from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenRejectTransactionBody(_message.Message):
    __slots__ = ("owner", "rejections")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    REJECTIONS_FIELD_NUMBER: _ClassVar[int]
    owner: _basic_types_pb2.AccountID
    rejections: _containers.RepeatedCompositeFieldContainer[TokenReference]
    def __init__(self, owner: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., rejections: _Optional[_Iterable[_Union[TokenReference, _Mapping]]] = ...) -> None: ...

class TokenReference(_message.Message):
    __slots__ = ("fungible_token", "nft")
    FUNGIBLE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NFT_FIELD_NUMBER: _ClassVar[int]
    fungible_token: _basic_types_pb2.TokenID
    nft: _basic_types_pb2.NftID
    def __init__(self, fungible_token: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., nft: _Optional[_Union[_basic_types_pb2.NftID, _Mapping]] = ...) -> None: ...
