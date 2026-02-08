from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UtilPrngTransactionBody(_message.Message):
    __slots__ = ("range",)
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: int
    def __init__(self, range: _Optional[int] = ...) -> None: ...
