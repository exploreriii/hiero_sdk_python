const CLOSING_REFERENCE_REGEX =
  /\b(?:fix(?:es|ed)?|close(?:s|d)?|resolve(?:s|d)?)\s*:?\s*((?:#\d+)(?:\s*(?:,|and)\s*#\d+)*)/gi;

function resolveExecutionContext(context) {
  const isDryRun = /^true$/i.test(process.env.DRY_RUN || "");
  const prNumber = Number(process.env.PR_NUMBER) || context.payload.pull_request?.number;
  return { prNumber, isDryRun, owner: context.repo.owner, repo: context.repo.repo };
}

function validatePrNumber(prNumber) {
  if (!prNumber) {
    throw new Error("PR number could not be determined.");
  }
}

function isBotAuthor(login = "") {
  return /\[bot\]$/i.test(login) || /dependabot/i.test(login);
}

function parseIssueNumbers(prBody) {
  const numbers = new Set();
  let match;
  while ((match = CLOSING_REFERENCE_REGEX.exec(prBody)) !== null) {
    const text = match[1] || "";
    for (const n of text.matchAll(/#(\d+)/g)) {
      numbers.add(Number(n[1]));
    }
  }
  return [...numbers];
}

function extractLabels(labelData) {
  const result = [];
  for (const item of labelData) {
    const name = typeof item === "string" ? item : item?.name;
    if (name?.trim()) {
      result.push(name.trim());
    }
  }
  return result;
}

async function fetchPrData(github, context, prNumber) {
  if (context.payload.pull_request) {
    return context.payload.pull_request;
  }
  const { data } = await github.rest.pulls.get({
    owner: context.repo.owner,
    repo: context.repo.repo,
    pull_number: prNumber,
  });
  return data;
}

function checkSkipConditions(prAuthor, linkedIssues) {
  if (isBotAuthor(prAuthor)) {
    return { skip: true, reason: `Skipping bot-authored PR from ${prAuthor}.` };
  }
  if (!linkedIssues.length) {
    return { skip: true, reason: "No linked issue references found in PR body." };
  }
  return { skip: false };
}

async function fetchIssueLabels(github, owner, repo, issueNumber) {
  try {
    const { data } = await github.rest.issues.get({ owner, repo, issue_number: issueNumber });
    if (data.pull_request) {
      console.log(`[sync] Skipping #${issueNumber}: is a PR reference.`);
      return [];
    }
    const labels = extractLabels(data.labels || []);
    console.log(`[sync] Issue #${issueNumber} labels: ${labels.length ? labels.join(", ") : "(none)"}`);
    return labels;
  } catch (err) {
    if (err?.status === 404) {
      console.log(`[sync] Issue #${issueNumber} not found. Skipping.`);
      return [];
    }
    throw err;
  }
}

function computeDelta(existingLabels, issueLabels) {
  const existing = new Set(existingLabels);
  return issueLabels.filter((l) => !existing.has(l));
}

function logResults(prNum, toAdd, existing) {
  console.log(`[sync] Processing PR #${prNum}.`);
  console.log(`[sync] Existing: ${existing.size ? [...existing].join(", ") : "(none)"}`);
  console.log(`[sync] To add: ${toAdd.length ? toAdd.join(", ") : "(none)"}`);
}

async function syncLabels({ github, context }) {
  const { prNumber, isDryRun, owner, repo } = resolveExecutionContext(context);
  validatePrNumber(prNumber);

  console.log(`[sync] Processing PR #${prNumber} in ${owner}/${repo} (dry_run=${isDryRun}).`);

  const prData = await fetchPrData(github, context, prNumber);
  const linkedIssues = parseIssueNumbers(prData?.body || "");

  const skip = checkSkipConditions(prData?.user?.login || "", linkedIssues);
  if (skip.skip) {
    console.log(`[sync] ${skip.reason}`);
    return { labels: [] };
  }

  console.log(`[sync] Linked issues: ${linkedIssues.map((n) => `#${n}`).join(", ")}`);

  const allLabels = [];
  for (const num of linkedIssues) {
    const labels = await fetchIssueLabels(github, owner, repo, num);
    allLabels.push(...labels);
  }

  if (!allLabels.length) {
    console.log("[sync] No labels on linked issues.");
    return { labels: [] };
  }

  const existing = extractLabels(prData?.labels || []);
  const toAdd = computeDelta(existing, allLabels);
  logResults(prNumber, toAdd, new Set(existing));

  if (!toAdd.length) {
    console.log("[sync] PR already has all labels.");
    return { labels: [] };
  }

  if (isDryRun) {
    console.log(`[sync] DRY_RUN: would add ${toAdd.join(", ")}`);
    return { labels: toAdd };
  }

  await github.rest.issues.addLabels({ owner, repo, issue_number: prNumber, labels: toAdd });
  console.log(`[sync] Added labels: ${toAdd.join(", ")}`);

  return { labels: toAdd };
}

module.exports = syncLabels;
