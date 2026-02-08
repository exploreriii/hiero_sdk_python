from . import timestamp_pb2 as _timestamp_pb2
from . import basic_types_pb2 as _basic_types_pb2
from . import freeze_type_pb2 as _freeze_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FreezeTransactionBody(_message.Message):
    __slots__ = ("startHour", "startMin", "endHour", "endMin", "update_file", "file_hash", "start_time", "freeze_type")
    STARTHOUR_FIELD_NUMBER: _ClassVar[int]
    STARTMIN_FIELD_NUMBER: _ClassVar[int]
    ENDHOUR_FIELD_NUMBER: _ClassVar[int]
    ENDMIN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    FREEZE_TYPE_FIELD_NUMBER: _ClassVar[int]
    startHour: int
    startMin: int
    endHour: int
    endMin: int
    update_file: _basic_types_pb2.FileID
    file_hash: bytes
    start_time: _timestamp_pb2.Timestamp
    freeze_type: _freeze_type_pb2.FreezeType
    def __init__(self, startHour: _Optional[int] = ..., startMin: _Optional[int] = ..., endHour: _Optional[int] = ..., endMin: _Optional[int] = ..., update_file: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., file_hash: _Optional[bytes] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., freeze_type: _Optional[_Union[_freeze_type_pb2.FreezeType, str]] = ...) -> None: ...
