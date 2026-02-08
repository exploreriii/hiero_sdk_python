from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoTransferTransactionBody(_message.Message):
    __slots__ = ("transfers", "tokenTransfers")
    TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    TOKENTRANSFERS_FIELD_NUMBER: _ClassVar[int]
    transfers: _basic_types_pb2.TransferList
    tokenTransfers: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenTransferList]
    def __init__(self, transfers: _Optional[_Union[_basic_types_pb2.TransferList, _Mapping]] = ..., tokenTransfers: _Optional[_Iterable[_Union[_basic_types_pb2.TokenTransferList, _Mapping]]] = ...) -> None: ...
