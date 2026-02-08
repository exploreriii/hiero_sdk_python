from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UncheckedSubmitBody(_message.Message):
    __slots__ = ("transactionBytes",)
    TRANSACTIONBYTES_FIELD_NUMBER: _ClassVar[int]
    transactionBytes: bytes
    def __init__(self, transactionBytes: _Optional[bytes] = ...) -> None: ...
