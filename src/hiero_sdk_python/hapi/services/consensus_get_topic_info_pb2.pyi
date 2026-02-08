from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from . import consensus_topic_info_pb2 as _consensus_topic_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsensusGetTopicInfoQuery(_message.Message):
    __slots__ = ("header", "topicID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    topicID: _basic_types_pb2.TopicID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., topicID: _Optional[_Union[_basic_types_pb2.TopicID, _Mapping]] = ...) -> None: ...

class ConsensusGetTopicInfoResponse(_message.Message):
    __slots__ = ("header", "topicID", "topicInfo")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    TOPICINFO_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    topicID: _basic_types_pb2.TopicID
    topicInfo: _consensus_topic_info_pb2.ConsensusTopicInfo
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., topicID: _Optional[_Union[_basic_types_pb2.TopicID, _Mapping]] = ..., topicInfo: _Optional[_Union[_consensus_topic_info_pb2.ConsensusTopicInfo, _Mapping]] = ...) -> None: ...
