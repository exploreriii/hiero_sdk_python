from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HintsPartialSignatureTransactionBody(_message.Message):
    __slots__ = ("construction_id", "message", "partial_signature")
    CONSTRUCTION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    construction_id: int
    message: bytes
    partial_signature: bytes
    def __init__(self, construction_id: _Optional[int] = ..., message: _Optional[bytes] = ..., partial_signature: _Optional[bytes] = ...) -> None: ...
