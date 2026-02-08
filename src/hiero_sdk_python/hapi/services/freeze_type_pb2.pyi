from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FreezeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_FREEZE_TYPE: _ClassVar[FreezeType]
    FREEZE_ONLY: _ClassVar[FreezeType]
    PREPARE_UPGRADE: _ClassVar[FreezeType]
    FREEZE_UPGRADE: _ClassVar[FreezeType]
    FREEZE_ABORT: _ClassVar[FreezeType]
    TELEMETRY_UPGRADE: _ClassVar[FreezeType]
UNKNOWN_FREEZE_TYPE: FreezeType
FREEZE_ONLY: FreezeType
PREPARE_UPGRADE: FreezeType
FREEZE_UPGRADE: FreezeType
FREEZE_ABORT: FreezeType
TELEMETRY_UPGRADE: FreezeType
