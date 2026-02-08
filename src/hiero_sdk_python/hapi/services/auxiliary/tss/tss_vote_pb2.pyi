from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TssVoteTransactionBody(_message.Message):
    __slots__ = ("source_roster_hash", "target_roster_hash", "ledger_id", "node_signature", "tss_vote")
    SOURCE_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TSS_VOTE_FIELD_NUMBER: _ClassVar[int]
    source_roster_hash: bytes
    target_roster_hash: bytes
    ledger_id: bytes
    node_signature: bytes
    tss_vote: bytes
    def __init__(self, source_roster_hash: _Optional[bytes] = ..., target_roster_hash: _Optional[bytes] = ..., ledger_id: _Optional[bytes] = ..., node_signature: _Optional[bytes] = ..., tss_vote: _Optional[bytes] = ...) -> None: ...
