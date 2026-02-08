from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenFreezeAccountTransactionBody(_message.Message):
    __slots__ = ("token", "account")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    token: _basic_types_pb2.TokenID
    account: _basic_types_pb2.AccountID
    def __init__(self, token: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., account: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...
