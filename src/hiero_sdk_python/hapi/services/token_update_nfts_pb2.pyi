from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenUpdateNftsTransactionBody(_message.Message):
    __slots__ = ("token", "serial_numbers", "metadata")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    token: _basic_types_pb2.TokenID
    serial_numbers: _containers.RepeatedScalarFieldContainer[int]
    metadata: _wrappers_pb2.BytesValue
    def __init__(self, token: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., serial_numbers: _Optional[_Iterable[int]] = ..., metadata: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...
