from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenAssociateTransactionBody(_message.Message):
    __slots__ = ("account", "tokens")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    account: _basic_types_pb2.AccountID
    tokens: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenID]
    def __init__(self, account: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., tokens: _Optional[_Iterable[_Union[_basic_types_pb2.TokenID, _Mapping]]] = ...) -> None: ...
