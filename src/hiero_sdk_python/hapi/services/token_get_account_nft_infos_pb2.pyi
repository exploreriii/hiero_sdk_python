from . import basic_types_pb2 as _basic_types_pb2
from . import token_get_nft_info_pb2 as _token_get_nft_info_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenGetAccountNftInfosQuery(_message.Message):
    __slots__ = ("header", "accountID", "start", "end")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    accountID: _basic_types_pb2.AccountID
    start: int
    end: int
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class TokenGetAccountNftInfosResponse(_message.Message):
    __slots__ = ("header", "nfts")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NFTS_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    nfts: _containers.RepeatedCompositeFieldContainer[_token_get_nft_info_pb2.TokenNftInfo]
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., nfts: _Optional[_Iterable[_Union[_token_get_nft_info_pb2.TokenNftInfo, _Mapping]]] = ...) -> None: ...
