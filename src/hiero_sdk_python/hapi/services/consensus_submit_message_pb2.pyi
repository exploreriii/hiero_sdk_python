from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsensusMessageChunkInfo(_message.Message):
    __slots__ = ("initialTransactionID", "total", "number")
    INITIALTRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    initialTransactionID: _basic_types_pb2.TransactionID
    total: int
    number: int
    def __init__(self, initialTransactionID: _Optional[_Union[_basic_types_pb2.TransactionID, _Mapping]] = ..., total: _Optional[int] = ..., number: _Optional[int] = ...) -> None: ...

class ConsensusSubmitMessageTransactionBody(_message.Message):
    __slots__ = ("topicID", "message", "chunkInfo")
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHUNKINFO_FIELD_NUMBER: _ClassVar[int]
    topicID: _basic_types_pb2.TopicID
    message: bytes
    chunkInfo: ConsensusMessageChunkInfo
    def __init__(self, topicID: _Optional[_Union[_basic_types_pb2.TopicID, _Mapping]] = ..., message: _Optional[bytes] = ..., chunkInfo: _Optional[_Union[ConsensusMessageChunkInfo, _Mapping]] = ...) -> None: ...
