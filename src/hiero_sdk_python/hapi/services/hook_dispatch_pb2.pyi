from . import basic_types_pb2 as _basic_types_pb2
from . import hook_types_pb2 as _hook_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HookDispatchTransactionBody(_message.Message):
    __slots__ = ("hook_id_to_delete", "creation", "execution")
    HOOK_ID_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    CREATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    hook_id_to_delete: _basic_types_pb2.HookId
    creation: _hook_types_pb2.HookCreation
    execution: HookExecution
    def __init__(self, hook_id_to_delete: _Optional[_Union[_basic_types_pb2.HookId, _Mapping]] = ..., creation: _Optional[_Union[_hook_types_pb2.HookCreation, _Mapping]] = ..., execution: _Optional[_Union[HookExecution, _Mapping]] = ...) -> None: ...

class HookExecution(_message.Message):
    __slots__ = ("hook_entity_id", "call")
    HOOK_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    hook_entity_id: _basic_types_pb2.HookEntityId
    call: _basic_types_pb2.HookCall
    def __init__(self, hook_entity_id: _Optional[_Union[_basic_types_pb2.HookEntityId, _Mapping]] = ..., call: _Optional[_Union[_basic_types_pb2.HookCall, _Mapping]] = ...) -> None: ...
