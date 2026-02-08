from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TssMessageTransactionBody(_message.Message):
    __slots__ = ("source_roster_hash", "target_roster_hash", "share_index", "tss_message")
    SOURCE_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    SHARE_INDEX_FIELD_NUMBER: _ClassVar[int]
    TSS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    source_roster_hash: bytes
    target_roster_hash: bytes
    share_index: int
    tss_message: bytes
    def __init__(self, source_roster_hash: _Optional[bytes] = ..., target_roster_hash: _Optional[bytes] = ..., share_index: _Optional[int] = ..., tss_message: _Optional[bytes] = ...) -> None: ...
