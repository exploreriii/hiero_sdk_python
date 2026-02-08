from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoApproveAllowanceTransactionBody(_message.Message):
    __slots__ = ("cryptoAllowances", "nftAllowances", "tokenAllowances")
    CRYPTOALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    NFTALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    TOKENALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    cryptoAllowances: _containers.RepeatedCompositeFieldContainer[CryptoAllowance]
    nftAllowances: _containers.RepeatedCompositeFieldContainer[NftAllowance]
    tokenAllowances: _containers.RepeatedCompositeFieldContainer[TokenAllowance]
    def __init__(self, cryptoAllowances: _Optional[_Iterable[_Union[CryptoAllowance, _Mapping]]] = ..., nftAllowances: _Optional[_Iterable[_Union[NftAllowance, _Mapping]]] = ..., tokenAllowances: _Optional[_Iterable[_Union[TokenAllowance, _Mapping]]] = ...) -> None: ...

class CryptoAllowance(_message.Message):
    __slots__ = ("owner", "spender", "amount")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SPENDER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    owner: _basic_types_pb2.AccountID
    spender: _basic_types_pb2.AccountID
    amount: int
    def __init__(self, owner: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., spender: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., amount: _Optional[int] = ...) -> None: ...

class NftAllowance(_message.Message):
    __slots__ = ("tokenId", "owner", "spender", "serial_numbers", "approved_for_all", "delegating_spender")
    TOKENID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SPENDER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FOR_ALL_FIELD_NUMBER: _ClassVar[int]
    DELEGATING_SPENDER_FIELD_NUMBER: _ClassVar[int]
    tokenId: _basic_types_pb2.TokenID
    owner: _basic_types_pb2.AccountID
    spender: _basic_types_pb2.AccountID
    serial_numbers: _containers.RepeatedScalarFieldContainer[int]
    approved_for_all: _wrappers_pb2.BoolValue
    delegating_spender: _basic_types_pb2.AccountID
    def __init__(self, tokenId: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., owner: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., spender: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., serial_numbers: _Optional[_Iterable[int]] = ..., approved_for_all: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., delegating_spender: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class TokenAllowance(_message.Message):
    __slots__ = ("tokenId", "owner", "spender", "amount")
    TOKENID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SPENDER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    tokenId: _basic_types_pb2.TokenID
    owner: _basic_types_pb2.AccountID
    spender: _basic_types_pb2.AccountID
    amount: int
    def __init__(self, tokenId: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., owner: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., spender: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., amount: _Optional[int] = ...) -> None: ...
