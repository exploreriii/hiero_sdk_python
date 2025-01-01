from datetime import datetime
from hedera_sdk_python.hapi.basic_types_pb2 import Key, AccountID
from hedera_sdk_python.hapi.timestamp_pb2 import Timestamp
from hedera_sdk_python.hapi.duration_pb2 import Duration

class TopicInfo:
    """
    Represents the information retrieved from ConsensusService.getTopicInfo() about a topic.
    """

    def __init__(
        self,
        memo: str,
        running_hash: bytes,
        sequence_number: int,
        expiration_time: Timestamp,
        admin_key: Key,
        submit_key: Key,
        auto_renew_period: Duration,
        auto_renew_account: AccountID,
        ledger_id: bytes,
    ):
        self.memo = memo
        self.running_hash = running_hash
        self.sequence_number = sequence_number
        self.expiration_time = expiration_time
        self.admin_key = admin_key
        self.submit_key = submit_key
        self.auto_renew_period = auto_renew_period
        self.auto_renew_account = auto_renew_account
        self.ledger_id = ledger_id 

    @classmethod
    def from_proto(cls, topic_info_proto):
        """
        Constructs a TopicInfo object from a protobuf ConsensusTopicInfo message.
        If 'ledger_id' (snake_case) doesn't exist in your environment, this won't break.
        """
        return cls(
            memo=topic_info_proto.memo,
            running_hash=topic_info_proto.runningHash,
            sequence_number=topic_info_proto.sequenceNumber,
            expiration_time=topic_info_proto.expirationTime
                if topic_info_proto.HasField("expirationTime") else None,
            admin_key=(
                topic_info_proto.adminKey
                if topic_info_proto.HasField("adminKey") else None
            ),
            submit_key=(
                topic_info_proto.submitKey
                if topic_info_proto.HasField("submitKey") else None
            ),
            auto_renew_period=(
                topic_info_proto.autoRenewPeriod
                if topic_info_proto.HasField("autoRenewPeriod") else None
            ),
            auto_renew_account=(
                topic_info_proto.autoRenewAccount
                if topic_info_proto.HasField("autoRenewAccount") else None
            ),
            ledger_id=getattr(topic_info_proto, "ledger_id", None),
        )

    def __repr__(self):
        return (
            f"TopicInfo(memo={self.memo!r}, running_hash={self.running_hash!r}, "
            f"sequence_number={self.sequence_number}, expiration_time={self.expiration_time}, "
            f"admin_key={self.admin_key}, submit_key={self.submit_key}, "
            f"auto_renew_period={self.auto_renew_period}, auto_renew_account={self.auto_renew_account}, "
            f"ledger_id={self.ledger_id!r})"
        )

    def __str__(self):
        """
        Pretty-print similar to __repr__, but multiline if you prefer.
        """
        dt_str = None
        if self.expiration_time and hasattr(self.expiration_time, "seconds"):
            dt_str = datetime.fromtimestamp(self.expiration_time.seconds)

        return (
            "TopicInfo(\n"
            f"  memo={self.memo!r},\n"
            f"  running_hash={self.running_hash!r},\n"
            f"  sequence_number={self.sequence_number},\n"
            f"  expiration_time={dt_str},\n"
            f"  admin_key={self.admin_key},\n"
            f"  submit_key={self.submit_key},\n"
            f"  auto_renew_period={self.auto_renew_period},\n"
            f"  auto_renew_account={self.auto_renew_account},\n"
            f"  ledger_id={self.ledger_id!r}\n"
            ")"
        )
