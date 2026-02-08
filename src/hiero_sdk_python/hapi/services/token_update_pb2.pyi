from . import basic_types_pb2 as _basic_types_pb2
from . import duration_pb2 as _duration_pb2
from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenUpdateTransactionBody(_message.Message):
    __slots__ = ("token", "symbol", "name", "treasury", "adminKey", "kycKey", "freezeKey", "wipeKey", "supplyKey", "autoRenewAccount", "autoRenewPeriod", "expiry", "memo", "fee_schedule_key", "pause_key", "metadata", "metadata_key", "key_verification_mode")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TREASURY_FIELD_NUMBER: _ClassVar[int]
    ADMINKEY_FIELD_NUMBER: _ClassVar[int]
    KYCKEY_FIELD_NUMBER: _ClassVar[int]
    FREEZEKEY_FIELD_NUMBER: _ClassVar[int]
    WIPEKEY_FIELD_NUMBER: _ClassVar[int]
    SUPPLYKEY_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    FEE_SCHEDULE_KEY_FIELD_NUMBER: _ClassVar[int]
    PAUSE_KEY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_VERIFICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    token: _basic_types_pb2.TokenID
    symbol: str
    name: str
    treasury: _basic_types_pb2.AccountID
    adminKey: _basic_types_pb2.Key
    kycKey: _basic_types_pb2.Key
    freezeKey: _basic_types_pb2.Key
    wipeKey: _basic_types_pb2.Key
    supplyKey: _basic_types_pb2.Key
    autoRenewAccount: _basic_types_pb2.AccountID
    autoRenewPeriod: _duration_pb2.Duration
    expiry: _timestamp_pb2.Timestamp
    memo: _wrappers_pb2.StringValue
    fee_schedule_key: _basic_types_pb2.Key
    pause_key: _basic_types_pb2.Key
    metadata: _wrappers_pb2.BytesValue
    metadata_key: _basic_types_pb2.Key
    key_verification_mode: _basic_types_pb2.TokenKeyValidation
    def __init__(self, token: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., symbol: _Optional[str] = ..., name: _Optional[str] = ..., treasury: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., kycKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., freezeKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., wipeKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., supplyKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., autoRenewAccount: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., memo: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., fee_schedule_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., pause_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., metadata: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., metadata_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., key_verification_mode: _Optional[_Union[_basic_types_pb2.TokenKeyValidation, str]] = ...) -> None: ...
