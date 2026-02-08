from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractCallTransactionBody(_message.Message):
    __slots__ = ("contractID", "gas", "amount", "functionParameters")
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    contractID: _basic_types_pb2.ContractID
    gas: int
    amount: int
    functionParameters: bytes
    def __init__(self, contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., gas: _Optional[int] = ..., amount: _Optional[int] = ..., functionParameters: _Optional[bytes] = ...) -> None: ...
