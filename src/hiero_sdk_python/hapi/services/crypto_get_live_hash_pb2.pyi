from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from . import crypto_add_live_hash_pb2 as _crypto_add_live_hash_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoGetLiveHashQuery(_message.Message):
    __slots__ = ("header", "accountID", "hash")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    accountID: _basic_types_pb2.AccountID
    hash: bytes
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., hash: _Optional[bytes] = ...) -> None: ...

class CryptoGetLiveHashResponse(_message.Message):
    __slots__ = ("header", "liveHash")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    LIVEHASH_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    liveHash: _crypto_add_live_hash_pb2.LiveHash
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., liveHash: _Optional[_Union[_crypto_add_live_hash_pb2.LiveHash, _Mapping]] = ...) -> None: ...
