from . import timestamp_pb2 as _timestamp_pb2
from . import duration_pb2 as _duration_pb2
from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAccountDetailsQuery(_message.Message):
    __slots__ = ("header", "account_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    account_id: _basic_types_pb2.AccountID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class GetAccountDetailsResponse(_message.Message):
    __slots__ = ("header", "account_details")
    class AccountDetails(_message.Message):
        __slots__ = ("account_id", "contract_account_id", "deleted", "proxy_account_id", "proxy_received", "key", "balance", "receiver_sig_required", "expiration_time", "auto_renew_period", "token_relationships", "memo", "owned_nfts", "max_automatic_token_associations", "alias", "ledger_id", "granted_crypto_allowances", "granted_nft_allowances", "granted_token_allowances")
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        PROXY_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        PROXY_RECEIVED_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        RECEIVER_SIG_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
        AUTO_RENEW_PERIOD_FIELD_NUMBER: _ClassVar[int]
        TOKEN_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
        MEMO_FIELD_NUMBER: _ClassVar[int]
        OWNED_NFTS_FIELD_NUMBER: _ClassVar[int]
        MAX_AUTOMATIC_TOKEN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
        GRANTED_CRYPTO_ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
        GRANTED_NFT_ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
        GRANTED_TOKEN_ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
        account_id: _basic_types_pb2.AccountID
        contract_account_id: str
        deleted: bool
        proxy_account_id: _basic_types_pb2.AccountID
        proxy_received: int
        key: _basic_types_pb2.Key
        balance: int
        receiver_sig_required: bool
        expiration_time: _timestamp_pb2.Timestamp
        auto_renew_period: _duration_pb2.Duration
        token_relationships: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenRelationship]
        memo: str
        owned_nfts: int
        max_automatic_token_associations: int
        alias: bytes
        ledger_id: bytes
        granted_crypto_allowances: _containers.RepeatedCompositeFieldContainer[GrantedCryptoAllowance]
        granted_nft_allowances: _containers.RepeatedCompositeFieldContainer[GrantedNftAllowance]
        granted_token_allowances: _containers.RepeatedCompositeFieldContainer[GrantedTokenAllowance]
        def __init__(self, account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., contract_account_id: _Optional[str] = ..., deleted: bool = ..., proxy_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., proxy_received: _Optional[int] = ..., key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., balance: _Optional[int] = ..., receiver_sig_required: bool = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auto_renew_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., token_relationships: _Optional[_Iterable[_Union[_basic_types_pb2.TokenRelationship, _Mapping]]] = ..., memo: _Optional[str] = ..., owned_nfts: _Optional[int] = ..., max_automatic_token_associations: _Optional[int] = ..., alias: _Optional[bytes] = ..., ledger_id: _Optional[bytes] = ..., granted_crypto_allowances: _Optional[_Iterable[_Union[GrantedCryptoAllowance, _Mapping]]] = ..., granted_nft_allowances: _Optional[_Iterable[_Union[GrantedNftAllowance, _Mapping]]] = ..., granted_token_allowances: _Optional[_Iterable[_Union[GrantedTokenAllowance, _Mapping]]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    account_details: GetAccountDetailsResponse.AccountDetails
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., account_details: _Optional[_Union[GetAccountDetailsResponse.AccountDetails, _Mapping]] = ...) -> None: ...

class GrantedCryptoAllowance(_message.Message):
    __slots__ = ("spender", "amount")
    SPENDER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    spender: _basic_types_pb2.AccountID
    amount: int
    def __init__(self, spender: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., amount: _Optional[int] = ...) -> None: ...

class GrantedNftAllowance(_message.Message):
    __slots__ = ("token_id", "spender")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SPENDER_FIELD_NUMBER: _ClassVar[int]
    token_id: _basic_types_pb2.TokenID
    spender: _basic_types_pb2.AccountID
    def __init__(self, token_id: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., spender: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class GrantedTokenAllowance(_message.Message):
    __slots__ = ("token_id", "spender", "amount")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SPENDER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_id: _basic_types_pb2.TokenID
    spender: _basic_types_pb2.AccountID
    amount: int
    def __init__(self, token_id: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., spender: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., amount: _Optional[int] = ...) -> None: ...
