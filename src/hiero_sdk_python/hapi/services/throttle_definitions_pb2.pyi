from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ThrottleGroup(_message.Message):
    __slots__ = ("operations", "milliOpsPerSec")
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    MILLIOPSPERSEC_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedScalarFieldContainer[_basic_types_pb2.HederaFunctionality]
    milliOpsPerSec: int
    def __init__(self, operations: _Optional[_Iterable[_Union[_basic_types_pb2.HederaFunctionality, str]]] = ..., milliOpsPerSec: _Optional[int] = ...) -> None: ...

class ThrottleBucket(_message.Message):
    __slots__ = ("name", "burstPeriodMs", "throttleGroups")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BURSTPERIODMS_FIELD_NUMBER: _ClassVar[int]
    THROTTLEGROUPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    burstPeriodMs: int
    throttleGroups: _containers.RepeatedCompositeFieldContainer[ThrottleGroup]
    def __init__(self, name: _Optional[str] = ..., burstPeriodMs: _Optional[int] = ..., throttleGroups: _Optional[_Iterable[_Union[ThrottleGroup, _Mapping]]] = ...) -> None: ...

class ThrottleDefinitions(_message.Message):
    __slots__ = ("throttleBuckets",)
    THROTTLEBUCKETS_FIELD_NUMBER: _ClassVar[int]
    throttleBuckets: _containers.RepeatedCompositeFieldContainer[ThrottleBucket]
    def __init__(self, throttleBuckets: _Optional[_Iterable[_Union[ThrottleBucket, _Mapping]]] = ...) -> None: ...
