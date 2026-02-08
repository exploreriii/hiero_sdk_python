from . import basic_types_pb2 as _basic_types_pb2
from . import custom_fees_pb2 as _custom_fees_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from . import timestamp_pb2 as _timestamp_pb2
from . import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenGetInfoQuery(_message.Message):
    __slots__ = ("header", "token")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    token: _basic_types_pb2.TokenID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., token: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ...) -> None: ...

class TokenInfo(_message.Message):
    __slots__ = ("tokenId", "name", "symbol", "decimals", "totalSupply", "treasury", "adminKey", "kycKey", "freezeKey", "wipeKey", "supplyKey", "defaultFreezeStatus", "defaultKycStatus", "deleted", "autoRenewAccount", "autoRenewPeriod", "expiry", "memo", "tokenType", "supplyType", "maxSupply", "fee_schedule_key", "custom_fees", "pause_key", "pause_status", "ledger_id", "metadata", "metadata_key")
    TOKENID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    TOTALSUPPLY_FIELD_NUMBER: _ClassVar[int]
    TREASURY_FIELD_NUMBER: _ClassVar[int]
    ADMINKEY_FIELD_NUMBER: _ClassVar[int]
    KYCKEY_FIELD_NUMBER: _ClassVar[int]
    FREEZEKEY_FIELD_NUMBER: _ClassVar[int]
    WIPEKEY_FIELD_NUMBER: _ClassVar[int]
    SUPPLYKEY_FIELD_NUMBER: _ClassVar[int]
    DEFAULTFREEZESTATUS_FIELD_NUMBER: _ClassVar[int]
    DEFAULTKYCSTATUS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    TOKENTYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPLYTYPE_FIELD_NUMBER: _ClassVar[int]
    MAXSUPPLY_FIELD_NUMBER: _ClassVar[int]
    FEE_SCHEDULE_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEES_FIELD_NUMBER: _ClassVar[int]
    PAUSE_KEY_FIELD_NUMBER: _ClassVar[int]
    PAUSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_KEY_FIELD_NUMBER: _ClassVar[int]
    tokenId: _basic_types_pb2.TokenID
    name: str
    symbol: str
    decimals: int
    totalSupply: int
    treasury: _basic_types_pb2.AccountID
    adminKey: _basic_types_pb2.Key
    kycKey: _basic_types_pb2.Key
    freezeKey: _basic_types_pb2.Key
    wipeKey: _basic_types_pb2.Key
    supplyKey: _basic_types_pb2.Key
    defaultFreezeStatus: _basic_types_pb2.TokenFreezeStatus
    defaultKycStatus: _basic_types_pb2.TokenKycStatus
    deleted: bool
    autoRenewAccount: _basic_types_pb2.AccountID
    autoRenewPeriod: _duration_pb2.Duration
    expiry: _timestamp_pb2.Timestamp
    memo: str
    tokenType: _basic_types_pb2.TokenType
    supplyType: _basic_types_pb2.TokenSupplyType
    maxSupply: int
    fee_schedule_key: _basic_types_pb2.Key
    custom_fees: _containers.RepeatedCompositeFieldContainer[_custom_fees_pb2.CustomFee]
    pause_key: _basic_types_pb2.Key
    pause_status: _basic_types_pb2.TokenPauseStatus
    ledger_id: bytes
    metadata: bytes
    metadata_key: _basic_types_pb2.Key
    def __init__(self, tokenId: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., decimals: _Optional[int] = ..., totalSupply: _Optional[int] = ..., treasury: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., kycKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., freezeKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., wipeKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., supplyKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., defaultFreezeStatus: _Optional[_Union[_basic_types_pb2.TokenFreezeStatus, str]] = ..., defaultKycStatus: _Optional[_Union[_basic_types_pb2.TokenKycStatus, str]] = ..., deleted: bool = ..., autoRenewAccount: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., memo: _Optional[str] = ..., tokenType: _Optional[_Union[_basic_types_pb2.TokenType, str]] = ..., supplyType: _Optional[_Union[_basic_types_pb2.TokenSupplyType, str]] = ..., maxSupply: _Optional[int] = ..., fee_schedule_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., custom_fees: _Optional[_Iterable[_Union[_custom_fees_pb2.CustomFee, _Mapping]]] = ..., pause_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., pause_status: _Optional[_Union[_basic_types_pb2.TokenPauseStatus, str]] = ..., ledger_id: _Optional[bytes] = ..., metadata: _Optional[bytes] = ..., metadata_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ...) -> None: ...

class TokenGetInfoResponse(_message.Message):
    __slots__ = ("header", "tokenInfo")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TOKENINFO_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    tokenInfo: TokenInfo
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., tokenInfo: _Optional[_Union[TokenInfo, _Mapping]] = ...) -> None: ...
