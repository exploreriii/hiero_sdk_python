from . import basic_types_pb2 as _basic_types_pb2
from . import duration_pb2 as _duration_pb2
from . import hook_types_pb2 as _hook_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractCreateTransactionBody(_message.Message):
    __slots__ = ("fileID", "initcode", "adminKey", "gas", "initialBalance", "proxyAccountID", "autoRenewPeriod", "constructorParameters", "shardID", "realmID", "newRealmAdminKey", "memo", "max_automatic_token_associations", "auto_renew_account_id", "staked_account_id", "staked_node_id", "decline_reward", "hook_creation_details")
    FILEID_FIELD_NUMBER: _ClassVar[int]
    INITCODE_FIELD_NUMBER: _ClassVar[int]
    ADMINKEY_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    INITIALBALANCE_FIELD_NUMBER: _ClassVar[int]
    PROXYACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTORPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SHARDID_FIELD_NUMBER: _ClassVar[int]
    REALMID_FIELD_NUMBER: _ClassVar[int]
    NEWREALMADMINKEY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    MAX_AUTOMATIC_TOKEN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_RENEW_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STAKED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STAKED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DECLINE_REWARD_FIELD_NUMBER: _ClassVar[int]
    HOOK_CREATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    fileID: _basic_types_pb2.FileID
    initcode: bytes
    adminKey: _basic_types_pb2.Key
    gas: int
    initialBalance: int
    proxyAccountID: _basic_types_pb2.AccountID
    autoRenewPeriod: _duration_pb2.Duration
    constructorParameters: bytes
    shardID: _basic_types_pb2.ShardID
    realmID: _basic_types_pb2.RealmID
    newRealmAdminKey: _basic_types_pb2.Key
    memo: str
    max_automatic_token_associations: int
    auto_renew_account_id: _basic_types_pb2.AccountID
    staked_account_id: _basic_types_pb2.AccountID
    staked_node_id: int
    decline_reward: bool
    hook_creation_details: _containers.RepeatedCompositeFieldContainer[_hook_types_pb2.HookCreationDetails]
    def __init__(self, fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., initcode: _Optional[bytes] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., gas: _Optional[int] = ..., initialBalance: _Optional[int] = ..., proxyAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., constructorParameters: _Optional[bytes] = ..., shardID: _Optional[_Union[_basic_types_pb2.ShardID, _Mapping]] = ..., realmID: _Optional[_Union[_basic_types_pb2.RealmID, _Mapping]] = ..., newRealmAdminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., memo: _Optional[str] = ..., max_automatic_token_associations: _Optional[int] = ..., auto_renew_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., staked_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., staked_node_id: _Optional[int] = ..., decline_reward: bool = ..., hook_creation_details: _Optional[_Iterable[_Union[_hook_types_pb2.HookCreationDetails, _Mapping]]] = ...) -> None: ...
