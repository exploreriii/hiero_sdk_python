from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkGetExecutionTimeQuery(_message.Message):
    __slots__ = ("header", "transaction_ids")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDS_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    transaction_ids: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TransactionID]
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., transaction_ids: _Optional[_Iterable[_Union[_basic_types_pb2.TransactionID, _Mapping]]] = ...) -> None: ...

class NetworkGetExecutionTimeResponse(_message.Message):
    __slots__ = ("header", "execution_times")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIMES_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    execution_times: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., execution_times: _Optional[_Iterable[int]] = ...) -> None: ...
