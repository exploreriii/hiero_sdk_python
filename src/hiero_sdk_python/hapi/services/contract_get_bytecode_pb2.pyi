from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractGetBytecodeQuery(_message.Message):
    __slots__ = ("header", "contractID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    contractID: _basic_types_pb2.ContractID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ...) -> None: ...

class ContractGetBytecodeResponse(_message.Message):
    __slots__ = ("header", "bytecode")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BYTECODE_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    bytecode: bytes
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., bytecode: _Optional[bytes] = ...) -> None: ...
