#!/usr/bin/env node

const { execSync } = require("child_process");

// These are the directories we want to check for correct naming
const TEST_DIRS = ["tests/unit", "tests/integration", "tests/tck", "tests/fuzz"];

// These are the excluded paths and file names inside the TEST_DIRS
const IGNORED = ["tests/fuzz/support"];
const EXCEPTIONS = ["conftest.py", "__init__.py", "init.py", "mock_server.py", "utils.py"];

// Collect naming errors to report at the end
const name_errors = [];

// Get list of changed files compared to main
const output = execSync("git diff --name-only origin/main...HEAD", { encoding: "utf-8" });
// Split output into lines and filter out empty lines for easy manipulation
// e.g. output = "tests/unit/my_test.py\ntests/integration/other_test.py"
const files = output.split("\n").filter(Boolean);


for (const file of files) {
  // --- PATH FILTERING ---
  // Skip files that are not in any of the specified test directories
  if (!TEST_DIRS.some(dir => file.startsWith(dir))) continue;

  // Skip ignored paths (e.g. helpers)
  if (IGNORED.some(path => file.startsWith(path))) continue;

  // Now we have file paths that we need to check for correct naming
  // e.g. file = "tests/unit/my_test.py"

  // --- Correct PATH now apply NAMING checks ---

  // Extract the file name from the path
  // e.g. from file = "tests/unit/my_test.py" get name = "my_test.py"
  const name = file.split("/").pop();

  // Skip allowed special files
  if (EXCEPTIONS.includes(name)) continue;

  // Enforce naming rule on files 
  if (!name.endsWith("_test.py")) {
    console.error(`::error file=${file}::Must end with '_test.py'`);
    name_errors.push(file);
  }
}

// Fail if any bad files found
if (name_errors.length > 0) {
  console.error("\nInvalid test files:");
  name_errors.forEach(f => console.error(`- ${f}`));
  process.exit(1);
}

console.log("All test filenames are valid");