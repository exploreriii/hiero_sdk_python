from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from . import crypto_add_live_hash_pb2 as _crypto_add_live_hash_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetByKeyQuery(_message.Message):
    __slots__ = ("header", "key")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    key: _basic_types_pb2.Key
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ...) -> None: ...

class EntityID(_message.Message):
    __slots__ = ("accountID", "liveHash", "fileID", "contractID")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    LIVEHASH_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    accountID: _basic_types_pb2.AccountID
    liveHash: _crypto_add_live_hash_pb2.LiveHash
    fileID: _basic_types_pb2.FileID
    contractID: _basic_types_pb2.ContractID
    def __init__(self, accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., liveHash: _Optional[_Union[_crypto_add_live_hash_pb2.LiveHash, _Mapping]] = ..., fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ...) -> None: ...

class GetByKeyResponse(_message.Message):
    __slots__ = ("header", "entities")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    entities: _containers.RepeatedCompositeFieldContainer[EntityID]
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[EntityID, _Mapping]]] = ...) -> None: ...
