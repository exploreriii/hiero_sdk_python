from . import basic_types_pb2 as _basic_types_pb2
from . import duration_pb2 as _duration_pb2
from . import hook_types_pb2 as _hook_types_pb2
from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractUpdateTransactionBody(_message.Message):
    __slots__ = ("contractID", "expirationTime", "adminKey", "proxyAccountID", "autoRenewPeriod", "fileID", "memo", "memoWrapper", "max_automatic_token_associations", "auto_renew_account_id", "staked_account_id", "staked_node_id", "decline_reward", "hook_ids_to_delete", "hook_creation_details")
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
    ADMINKEY_FIELD_NUMBER: _ClassVar[int]
    PROXYACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    MEMOWRAPPER_FIELD_NUMBER: _ClassVar[int]
    MAX_AUTOMATIC_TOKEN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_RENEW_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STAKED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STAKED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DECLINE_REWARD_FIELD_NUMBER: _ClassVar[int]
    HOOK_IDS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    HOOK_CREATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    contractID: _basic_types_pb2.ContractID
    expirationTime: _timestamp_pb2.Timestamp
    adminKey: _basic_types_pb2.Key
    proxyAccountID: _basic_types_pb2.AccountID
    autoRenewPeriod: _duration_pb2.Duration
    fileID: _basic_types_pb2.FileID
    memo: str
    memoWrapper: _wrappers_pb2.StringValue
    max_automatic_token_associations: _wrappers_pb2.Int32Value
    auto_renew_account_id: _basic_types_pb2.AccountID
    staked_account_id: _basic_types_pb2.AccountID
    staked_node_id: int
    decline_reward: _wrappers_pb2.BoolValue
    hook_ids_to_delete: _containers.RepeatedScalarFieldContainer[int]
    hook_creation_details: _containers.RepeatedCompositeFieldContainer[_hook_types_pb2.HookCreationDetails]
    def __init__(self, contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., proxyAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., memo: _Optional[str] = ..., memoWrapper: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., max_automatic_token_associations: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., auto_renew_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., staked_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., staked_node_id: _Optional[int] = ..., decline_reward: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., hook_ids_to_delete: _Optional[_Iterable[int]] = ..., hook_creation_details: _Optional[_Iterable[_Union[_hook_types_pb2.HookCreationDetails, _Mapping]]] = ...) -> None: ...
