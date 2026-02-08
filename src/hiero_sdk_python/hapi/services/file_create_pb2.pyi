from . import basic_types_pb2 as _basic_types_pb2
from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileCreateTransactionBody(_message.Message):
    __slots__ = ("expirationTime", "keys", "contents", "shardID", "realmID", "newRealmAdminKey", "memo")
    EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SHARDID_FIELD_NUMBER: _ClassVar[int]
    REALMID_FIELD_NUMBER: _ClassVar[int]
    NEWREALMADMINKEY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    expirationTime: _timestamp_pb2.Timestamp
    keys: _basic_types_pb2.KeyList
    contents: bytes
    shardID: _basic_types_pb2.ShardID
    realmID: _basic_types_pb2.RealmID
    newRealmAdminKey: _basic_types_pb2.Key
    memo: str
    def __init__(self, expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., keys: _Optional[_Union[_basic_types_pb2.KeyList, _Mapping]] = ..., contents: _Optional[bytes] = ..., shardID: _Optional[_Union[_basic_types_pb2.ShardID, _Mapping]] = ..., realmID: _Optional[_Union[_basic_types_pb2.RealmID, _Mapping]] = ..., newRealmAdminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., memo: _Optional[str] = ...) -> None: ...
