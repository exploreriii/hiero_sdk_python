from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetBySolidityIDQuery(_message.Message):
    __slots__ = ("header", "solidityID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SOLIDITYID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    solidityID: str
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., solidityID: _Optional[str] = ...) -> None: ...

class GetBySolidityIDResponse(_message.Message):
    __slots__ = ("header", "accountID", "fileID", "contractID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    accountID: _basic_types_pb2.AccountID
    fileID: _basic_types_pb2.FileID
    contractID: _basic_types_pb2.ContractID
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ...) -> None: ...
