from . import response_code_pb2 as _response_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionResponse(_message.Message):
    __slots__ = ("nodeTransactionPrecheckCode", "cost")
    NODETRANSACTIONPRECHECKCODE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    nodeTransactionPrecheckCode: _response_code_pb2.ResponseCodeEnum
    cost: int
    def __init__(self, nodeTransactionPrecheckCode: _Optional[_Union[_response_code_pb2.ResponseCodeEnum, str]] = ..., cost: _Optional[int] = ...) -> None: ...
