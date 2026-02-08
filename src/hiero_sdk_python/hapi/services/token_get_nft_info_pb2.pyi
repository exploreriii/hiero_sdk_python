from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenGetNftInfoQuery(_message.Message):
    __slots__ = ("header", "nftID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NFTID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    nftID: _basic_types_pb2.NftID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., nftID: _Optional[_Union[_basic_types_pb2.NftID, _Mapping]] = ...) -> None: ...

class TokenNftInfo(_message.Message):
    __slots__ = ("nftID", "accountID", "creationTime", "metadata", "ledger_id", "spender_id")
    NFTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    SPENDER_ID_FIELD_NUMBER: _ClassVar[int]
    nftID: _basic_types_pb2.NftID
    accountID: _basic_types_pb2.AccountID
    creationTime: _timestamp_pb2.Timestamp
    metadata: bytes
    ledger_id: bytes
    spender_id: _basic_types_pb2.AccountID
    def __init__(self, nftID: _Optional[_Union[_basic_types_pb2.NftID, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., creationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[bytes] = ..., ledger_id: _Optional[bytes] = ..., spender_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class TokenGetNftInfoResponse(_message.Message):
    __slots__ = ("header", "nft")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NFT_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    nft: TokenNftInfo
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., nft: _Optional[_Union[TokenNftInfo, _Mapping]] = ...) -> None: ...
