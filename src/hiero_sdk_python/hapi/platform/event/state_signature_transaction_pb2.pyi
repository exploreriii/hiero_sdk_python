from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StateSignatureTransaction(_message.Message):
    __slots__ = ("round", "signature", "hash")
    ROUND_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    round: int
    signature: bytes
    hash: bytes
    def __init__(self, round: _Optional[int] = ..., signature: _Optional[bytes] = ..., hash: _Optional[bytes] = ...) -> None: ...
