from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoGetAccountBalanceQuery(_message.Message):
    __slots__ = ("header", "accountID", "contractID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    accountID: _basic_types_pb2.AccountID
    contractID: _basic_types_pb2.ContractID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ...) -> None: ...

class CryptoGetAccountBalanceResponse(_message.Message):
    __slots__ = ("header", "accountID", "balance", "tokenBalances")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    TOKENBALANCES_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    accountID: _basic_types_pb2.AccountID
    balance: int
    tokenBalances: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenBalance]
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., balance: _Optional[int] = ..., tokenBalances: _Optional[_Iterable[_Union[_basic_types_pb2.TokenBalance, _Mapping]]] = ...) -> None: ...
