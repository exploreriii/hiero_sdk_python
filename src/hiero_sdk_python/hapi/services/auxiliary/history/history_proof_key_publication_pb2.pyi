from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HistoryProofKeyPublicationTransactionBody(_message.Message):
    __slots__ = ("proof_key",)
    PROOF_KEY_FIELD_NUMBER: _ClassVar[int]
    proof_key: bytes
    def __init__(self, proof_key: _Optional[bytes] = ...) -> None: ...
