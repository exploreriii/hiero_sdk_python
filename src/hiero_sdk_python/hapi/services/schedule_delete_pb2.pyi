from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleDeleteTransactionBody(_message.Message):
    __slots__ = ("scheduleID",)
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    scheduleID: _basic_types_pb2.ScheduleID
    def __init__(self, scheduleID: _Optional[_Union[_basic_types_pb2.ScheduleID, _Mapping]] = ...) -> None: ...
