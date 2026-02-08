from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeRate(_message.Message):
    __slots__ = ("hbarEquiv", "centEquiv", "expirationTime")
    HBAREQUIV_FIELD_NUMBER: _ClassVar[int]
    CENTEQUIV_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
    hbarEquiv: int
    centEquiv: int
    expirationTime: _timestamp_pb2.TimestampSeconds
    def __init__(self, hbarEquiv: _Optional[int] = ..., centEquiv: _Optional[int] = ..., expirationTime: _Optional[_Union[_timestamp_pb2.TimestampSeconds, _Mapping]] = ...) -> None: ...

class ExchangeRateSet(_message.Message):
    __slots__ = ("currentRate", "nextRate")
    CURRENTRATE_FIELD_NUMBER: _ClassVar[int]
    NEXTRATE_FIELD_NUMBER: _ClassVar[int]
    currentRate: ExchangeRate
    nextRate: ExchangeRate
    def __init__(self, currentRate: _Optional[_Union[ExchangeRate, _Mapping]] = ..., nextRate: _Optional[_Union[ExchangeRate, _Mapping]] = ...) -> None: ...
