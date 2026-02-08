from . import basic_types_pb2 as _basic_types_pb2
from . import duration_pb2 as _duration_pb2
from . import hook_types_pb2 as _hook_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoCreateTransactionBody(_message.Message):
    __slots__ = ("key", "initialBalance", "proxyAccountID", "sendRecordThreshold", "receiveRecordThreshold", "receiverSigRequired", "autoRenewPeriod", "shardID", "realmID", "newRealmAdminKey", "memo", "max_automatic_token_associations", "staked_account_id", "staked_node_id", "decline_reward", "alias", "hook_creation_details")
    KEY_FIELD_NUMBER: _ClassVar[int]
    INITIALBALANCE_FIELD_NUMBER: _ClassVar[int]
    PROXYACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SENDRECORDTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RECEIVERECORDTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RECEIVERSIGREQUIRED_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
    SHARDID_FIELD_NUMBER: _ClassVar[int]
    REALMID_FIELD_NUMBER: _ClassVar[int]
    NEWREALMADMINKEY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    MAX_AUTOMATIC_TOKEN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    STAKED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STAKED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DECLINE_REWARD_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    HOOK_CREATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    key: _basic_types_pb2.Key
    initialBalance: int
    proxyAccountID: _basic_types_pb2.AccountID
    sendRecordThreshold: int
    receiveRecordThreshold: int
    receiverSigRequired: bool
    autoRenewPeriod: _duration_pb2.Duration
    shardID: _basic_types_pb2.ShardID
    realmID: _basic_types_pb2.RealmID
    newRealmAdminKey: _basic_types_pb2.Key
    memo: str
    max_automatic_token_associations: int
    staked_account_id: _basic_types_pb2.AccountID
    staked_node_id: int
    decline_reward: bool
    alias: bytes
    hook_creation_details: _containers.RepeatedCompositeFieldContainer[_hook_types_pb2.HookCreationDetails]
    def __init__(self, key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., initialBalance: _Optional[int] = ..., proxyAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., sendRecordThreshold: _Optional[int] = ..., receiveRecordThreshold: _Optional[int] = ..., receiverSigRequired: bool = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., shardID: _Optional[_Union[_basic_types_pb2.ShardID, _Mapping]] = ..., realmID: _Optional[_Union[_basic_types_pb2.RealmID, _Mapping]] = ..., newRealmAdminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., memo: _Optional[str] = ..., max_automatic_token_associations: _Optional[int] = ..., staked_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., staked_node_id: _Optional[int] = ..., decline_reward: bool = ..., alias: _Optional[bytes] = ..., hook_creation_details: _Optional[_Iterable[_Union[_hook_types_pb2.HookCreationDetails, _Mapping]]] = ...) -> None: ...
