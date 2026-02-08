from . import query_header_pb2 as _query_header_pb2
from . import response_code_pb2 as _response_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseHeader(_message.Message):
    __slots__ = ("nodeTransactionPrecheckCode", "responseType", "cost", "stateProof")
    NODETRANSACTIONPRECHECKCODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSETYPE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    STATEPROOF_FIELD_NUMBER: _ClassVar[int]
    nodeTransactionPrecheckCode: _response_code_pb2.ResponseCodeEnum
    responseType: _query_header_pb2.ResponseType
    cost: int
    stateProof: bytes
    def __init__(self, nodeTransactionPrecheckCode: _Optional[_Union[_response_code_pb2.ResponseCodeEnum, str]] = ..., responseType: _Optional[_Union[_query_header_pb2.ResponseType, str]] = ..., cost: _Optional[int] = ..., stateProof: _Optional[bytes] = ...) -> None: ...
