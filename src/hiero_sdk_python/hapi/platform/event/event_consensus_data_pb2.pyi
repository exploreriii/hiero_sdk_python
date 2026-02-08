from ...services import basic_types_pb2 as _basic_types_pb2
from . import event_descriptor_pb2 as _event_descriptor_pb2
from ...services import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventConsensusData(_message.Message):
    __slots__ = ("consensus_timestamp", "consensus_order")
    CONSENSUS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_ORDER_FIELD_NUMBER: _ClassVar[int]
    consensus_timestamp: _timestamp_pb2.Timestamp
    consensus_order: int
    def __init__(self, consensus_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., consensus_order: _Optional[int] = ...) -> None: ...
