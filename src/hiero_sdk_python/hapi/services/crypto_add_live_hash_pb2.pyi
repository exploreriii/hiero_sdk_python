from . import basic_types_pb2 as _basic_types_pb2
from . import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiveHash(_message.Message):
    __slots__ = ("accountId", "hash", "keys", "duration")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    accountId: _basic_types_pb2.AccountID
    hash: bytes
    keys: _basic_types_pb2.KeyList
    duration: _duration_pb2.Duration
    def __init__(self, accountId: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., hash: _Optional[bytes] = ..., keys: _Optional[_Union[_basic_types_pb2.KeyList, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CryptoAddLiveHashTransactionBody(_message.Message):
    __slots__ = ("liveHash",)
    LIVEHASH_FIELD_NUMBER: _ClassVar[int]
    liveHash: LiveHash
    def __init__(self, liveHash: _Optional[_Union[LiveHash, _Mapping]] = ...) -> None: ...
