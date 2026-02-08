from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractDeleteTransactionBody(_message.Message):
    __slots__ = ("contractID", "transferAccountID", "transferContractID", "permanent_removal")
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    TRANSFERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    TRANSFERCONTRACTID_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    contractID: _basic_types_pb2.ContractID
    transferAccountID: _basic_types_pb2.AccountID
    transferContractID: _basic_types_pb2.ContractID
    permanent_removal: bool
    def __init__(self, contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., transferAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., transferContractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., permanent_removal: bool = ...) -> None: ...
