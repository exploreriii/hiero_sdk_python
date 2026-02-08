from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkGetVersionInfoQuery(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ...) -> None: ...

class NetworkGetVersionInfoResponse(_message.Message):
    __slots__ = ("header", "hapiProtoVersion", "hederaServicesVersion")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    HAPIPROTOVERSION_FIELD_NUMBER: _ClassVar[int]
    HEDERASERVICESVERSION_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    hapiProtoVersion: _basic_types_pb2.SemanticVersion
    hederaServicesVersion: _basic_types_pb2.SemanticVersion
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., hapiProtoVersion: _Optional[_Union[_basic_types_pb2.SemanticVersion, _Mapping]] = ..., hederaServicesVersion: _Optional[_Union[_basic_types_pb2.SemanticVersion, _Mapping]] = ...) -> None: ...
