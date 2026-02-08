from . import timestamp_pb2 as _timestamp_pb2
from . import duration_pb2 as _duration_pb2
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

class CryptoGetInfoQuery(_message.Message):
    __slots__ = ("header", "accountID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    accountID: _basic_types_pb2.AccountID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class CryptoGetInfoResponse(_message.Message):
    __slots__ = ("header", "accountInfo")
    class AccountInfo(_message.Message):
        __slots__ = ("accountID", "contractAccountID", "deleted", "proxyAccountID", "proxyReceived", "key", "balance", "generateSendRecordThreshold", "generateReceiveRecordThreshold", "receiverSigRequired", "expirationTime", "autoRenewPeriod", "liveHashes", "tokenRelationships", "memo", "ownedNfts", "max_automatic_token_associations", "alias", "ledger_id", "ethereum_nonce", "staking_info")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        CONTRACTACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        PROXYACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        PROXYRECEIVED_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        GENERATESENDRECORDTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
        GENERATERECEIVERECORDTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
        RECEIVERSIGREQUIRED_FIELD_NUMBER: _ClassVar[int]
        EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
        AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
        LIVEHASHES_FIELD_NUMBER: _ClassVar[int]
        TOKENRELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
        MEMO_FIELD_NUMBER: _ClassVar[int]
        OWNEDNFTS_FIELD_NUMBER: _ClassVar[int]
        MAX_AUTOMATIC_TOKEN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
        ETHEREUM_NONCE_FIELD_NUMBER: _ClassVar[int]
        STAKING_INFO_FIELD_NUMBER: _ClassVar[int]
        accountID: _basic_types_pb2.AccountID
        contractAccountID: str
        deleted: bool
        proxyAccountID: _basic_types_pb2.AccountID
        proxyReceived: int
        key: _basic_types_pb2.Key
        balance: int
        generateSendRecordThreshold: int
        generateReceiveRecordThreshold: int
        receiverSigRequired: bool
        expirationTime: _timestamp_pb2.Timestamp
        autoRenewPeriod: _duration_pb2.Duration
        liveHashes: _containers.RepeatedCompositeFieldContainer[_crypto_add_live_hash_pb2.LiveHash]
        tokenRelationships: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenRelationship]
        memo: str
        ownedNfts: int
        max_automatic_token_associations: int
        alias: bytes
        ledger_id: bytes
        ethereum_nonce: int
        staking_info: _basic_types_pb2.StakingInfo
        def __init__(self, accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., contractAccountID: _Optional[str] = ..., deleted: bool = ..., proxyAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., proxyReceived: _Optional[int] = ..., key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., balance: _Optional[int] = ..., generateSendRecordThreshold: _Optional[int] = ..., generateReceiveRecordThreshold: _Optional[int] = ..., receiverSigRequired: bool = ..., expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., liveHashes: _Optional[_Iterable[_Union[_crypto_add_live_hash_pb2.LiveHash, _Mapping]]] = ..., tokenRelationships: _Optional[_Iterable[_Union[_basic_types_pb2.TokenRelationship, _Mapping]]] = ..., memo: _Optional[str] = ..., ownedNfts: _Optional[int] = ..., max_automatic_token_associations: _Optional[int] = ..., alias: _Optional[bytes] = ..., ledger_id: _Optional[bytes] = ..., ethereum_nonce: _Optional[int] = ..., staking_info: _Optional[_Union[_basic_types_pb2.StakingInfo, _Mapping]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTINFO_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    accountInfo: CryptoGetInfoResponse.AccountInfo
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., accountInfo: _Optional[_Union[CryptoGetInfoResponse.AccountInfo, _Mapping]] = ...) -> None: ...
