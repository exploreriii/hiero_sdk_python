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

class ContractGetInfoQuery(_message.Message):
    __slots__ = ("header", "contractID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    contractID: _basic_types_pb2.ContractID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ...) -> None: ...

class ContractGetInfoResponse(_message.Message):
    __slots__ = ("header", "contractInfo")
    class ContractInfo(_message.Message):
        __slots__ = ("contractID", "accountID", "contractAccountID", "adminKey", "expirationTime", "autoRenewPeriod", "storage", "memo", "balance", "deleted", "tokenRelationships", "ledger_id", "auto_renew_account_id", "max_automatic_token_associations", "staking_info")
        CONTRACTID_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        CONTRACTACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        ADMINKEY_FIELD_NUMBER: _ClassVar[int]
        EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
        AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
        STORAGE_FIELD_NUMBER: _ClassVar[int]
        MEMO_FIELD_NUMBER: _ClassVar[int]
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        TOKENRELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
        LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
        AUTO_RENEW_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_AUTOMATIC_TOKEN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
        STAKING_INFO_FIELD_NUMBER: _ClassVar[int]
        contractID: _basic_types_pb2.ContractID
        accountID: _basic_types_pb2.AccountID
        contractAccountID: str
        adminKey: _basic_types_pb2.Key
        expirationTime: _timestamp_pb2.Timestamp
        autoRenewPeriod: _duration_pb2.Duration
        storage: int
        memo: str
        balance: int
        deleted: bool
        tokenRelationships: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenRelationship]
        ledger_id: bytes
        auto_renew_account_id: _basic_types_pb2.AccountID
        max_automatic_token_associations: int
        staking_info: _basic_types_pb2.StakingInfo
        def __init__(self, contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., contractAccountID: _Optional[str] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., storage: _Optional[int] = ..., memo: _Optional[str] = ..., balance: _Optional[int] = ..., deleted: bool = ..., tokenRelationships: _Optional[_Iterable[_Union[_basic_types_pb2.TokenRelationship, _Mapping]]] = ..., ledger_id: _Optional[bytes] = ..., auto_renew_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., max_automatic_token_associations: _Optional[int] = ..., staking_info: _Optional[_Union[_basic_types_pb2.StakingInfo, _Mapping]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTINFO_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    contractInfo: ContractGetInfoResponse.ContractInfo
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., contractInfo: _Optional[_Union[ContractGetInfoResponse.ContractInfo, _Mapping]] = ...) -> None: ...
