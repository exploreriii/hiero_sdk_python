from . import transaction_pb2 as _transaction_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANSWER_ONLY: _ClassVar[ResponseType]
    ANSWER_STATE_PROOF: _ClassVar[ResponseType]
    COST_ANSWER: _ClassVar[ResponseType]
    COST_ANSWER_STATE_PROOF: _ClassVar[ResponseType]
ANSWER_ONLY: ResponseType
ANSWER_STATE_PROOF: ResponseType
COST_ANSWER: ResponseType
COST_ANSWER_STATE_PROOF: ResponseType

class QueryHeader(_message.Message):
    __slots__ = ("payment", "responseType")
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSETYPE_FIELD_NUMBER: _ClassVar[int]
    payment: _transaction_pb2.Transaction
    responseType: ResponseType
    def __init__(self, payment: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ..., responseType: _Optional[_Union[ResponseType, str]] = ...) -> None: ...
