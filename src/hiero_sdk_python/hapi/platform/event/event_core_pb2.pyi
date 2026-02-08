from ...services import basic_types_pb2 as _basic_types_pb2
from . import event_descriptor_pb2 as _event_descriptor_pb2
from ...services import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventCore(_message.Message):
    __slots__ = ("creator_node_id", "birth_round", "time_created", "parents", "version")
    CREATOR_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BIRTH_ROUND_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    PARENTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    creator_node_id: int
    birth_round: int
    time_created: _timestamp_pb2.Timestamp
    parents: _containers.RepeatedCompositeFieldContainer[_event_descriptor_pb2.EventDescriptor]
    version: _basic_types_pb2.SemanticVersion
    def __init__(self, creator_node_id: _Optional[int] = ..., birth_round: _Optional[int] = ..., time_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., parents: _Optional[_Iterable[_Union[_event_descriptor_pb2.EventDescriptor, _Mapping]]] = ..., version: _Optional[_Union[_basic_types_pb2.SemanticVersion, _Mapping]] = ...) -> None: ...
