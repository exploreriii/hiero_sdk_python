from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HookExtensionPoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCOUNT_ALLOWANCE_HOOK: _ClassVar[HookExtensionPoint]
ACCOUNT_ALLOWANCE_HOOK: HookExtensionPoint

class HookCreation(_message.Message):
    __slots__ = ("entity_id", "details", "next_hook_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: _basic_types_pb2.HookEntityId
    details: HookCreationDetails
    next_hook_id: _wrappers_pb2.Int64Value
    def __init__(self, entity_id: _Optional[_Union[_basic_types_pb2.HookEntityId, _Mapping]] = ..., details: _Optional[_Union[HookCreationDetails, _Mapping]] = ..., next_hook_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class HookCreationDetails(_message.Message):
    __slots__ = ("extension_point", "hook_id", "pure_evm_hook", "lambda_evm_hook", "admin_key")
    EXTENSION_POINT_FIELD_NUMBER: _ClassVar[int]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    PURE_EVM_HOOK_FIELD_NUMBER: _ClassVar[int]
    LAMBDA_EVM_HOOK_FIELD_NUMBER: _ClassVar[int]
    ADMIN_KEY_FIELD_NUMBER: _ClassVar[int]
    extension_point: HookExtensionPoint
    hook_id: int
    pure_evm_hook: PureEvmHook
    lambda_evm_hook: LambdaEvmHook
    admin_key: _basic_types_pb2.Key
    def __init__(self, extension_point: _Optional[_Union[HookExtensionPoint, str]] = ..., hook_id: _Optional[int] = ..., pure_evm_hook: _Optional[_Union[PureEvmHook, _Mapping]] = ..., lambda_evm_hook: _Optional[_Union[LambdaEvmHook, _Mapping]] = ..., admin_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ...) -> None: ...

class PureEvmHook(_message.Message):
    __slots__ = ("spec",)
    SPEC_FIELD_NUMBER: _ClassVar[int]
    spec: EvmHookSpec
    def __init__(self, spec: _Optional[_Union[EvmHookSpec, _Mapping]] = ...) -> None: ...

class LambdaEvmHook(_message.Message):
    __slots__ = ("spec", "storage_updates")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    spec: EvmHookSpec
    storage_updates: _containers.RepeatedCompositeFieldContainer[LambdaStorageUpdate]
    def __init__(self, spec: _Optional[_Union[EvmHookSpec, _Mapping]] = ..., storage_updates: _Optional[_Iterable[_Union[LambdaStorageUpdate, _Mapping]]] = ...) -> None: ...

class EvmHookSpec(_message.Message):
    __slots__ = ("contract_id",)
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    contract_id: _basic_types_pb2.ContractID
    def __init__(self, contract_id: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ...) -> None: ...

class LambdaStorageUpdate(_message.Message):
    __slots__ = ("storage_slot", "mapping_entries")
    STORAGE_SLOT_FIELD_NUMBER: _ClassVar[int]
    MAPPING_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    storage_slot: LambdaStorageSlot
    mapping_entries: LambdaMappingEntries
    def __init__(self, storage_slot: _Optional[_Union[LambdaStorageSlot, _Mapping]] = ..., mapping_entries: _Optional[_Union[LambdaMappingEntries, _Mapping]] = ...) -> None: ...

class LambdaMappingEntries(_message.Message):
    __slots__ = ("mapping_slot", "entries")
    MAPPING_SLOT_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    mapping_slot: bytes
    entries: _containers.RepeatedCompositeFieldContainer[LambdaMappingEntry]
    def __init__(self, mapping_slot: _Optional[bytes] = ..., entries: _Optional[_Iterable[_Union[LambdaMappingEntry, _Mapping]]] = ...) -> None: ...

class LambdaMappingEntry(_message.Message):
    __slots__ = ("key", "preimage", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    preimage: bytes
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., preimage: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class LambdaStorageSlot(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...
