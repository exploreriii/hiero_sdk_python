from . import basic_types_pb2 as _basic_types_pb2
from . import hook_types_pb2 as _hook_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LambdaSStoreTransactionBody(_message.Message):
    __slots__ = ("hook_id", "storage_updates")
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    hook_id: _basic_types_pb2.HookId
    storage_updates: _containers.RepeatedCompositeFieldContainer[_hook_types_pb2.LambdaStorageUpdate]
    def __init__(self, hook_id: _Optional[_Union[_basic_types_pb2.HookId, _Mapping]] = ..., storage_updates: _Optional[_Iterable[_Union[_hook_types_pb2.LambdaStorageUpdate, _Mapping]]] = ...) -> None: ...
