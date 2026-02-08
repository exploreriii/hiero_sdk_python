from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EthereumTransactionBody(_message.Message):
    __slots__ = ("ethereum_data", "call_data", "max_gas_allowance")
    ETHEREUM_DATA_FIELD_NUMBER: _ClassVar[int]
    CALL_DATA_FIELD_NUMBER: _ClassVar[int]
    MAX_GAS_ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    ethereum_data: bytes
    call_data: _basic_types_pb2.FileID
    max_gas_allowance: int
    def __init__(self, ethereum_data: _Optional[bytes] = ..., call_data: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., max_gas_allowance: _Optional[int] = ...) -> None: ...
