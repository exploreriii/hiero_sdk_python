from . import basic_types_pb2 as _basic_types_pb2
from . import contract_types_pb2 as _contract_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractCallLocalQuery(_message.Message):
    __slots__ = ("header", "contractID", "gas", "functionParameters", "maxResultSize", "sender_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MAXRESULTSIZE_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    contractID: _basic_types_pb2.ContractID
    gas: int
    functionParameters: bytes
    maxResultSize: int
    sender_id: _basic_types_pb2.AccountID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., gas: _Optional[int] = ..., functionParameters: _Optional[bytes] = ..., maxResultSize: _Optional[int] = ..., sender_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class ContractCallLocalResponse(_message.Message):
    __slots__ = ("header", "functionResult")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONRESULT_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    functionResult: _contract_types_pb2.ContractFunctionResult
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., functionResult: _Optional[_Union[_contract_types_pb2.ContractFunctionResult, _Mapping]] = ...) -> None: ...
