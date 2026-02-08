from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenClaimAirdropTransactionBody(_message.Message):
    __slots__ = ("pending_airdrops",)
    PENDING_AIRDROPS_FIELD_NUMBER: _ClassVar[int]
    pending_airdrops: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.PendingAirdropId]
    def __init__(self, pending_airdrops: _Optional[_Iterable[_Union[_basic_types_pb2.PendingAirdropId, _Mapping]]] = ...) -> None: ...
