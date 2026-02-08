from . import transaction_record_pb2 as _transaction_record_pb2
from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionGetFastRecordQuery(_message.Message):
    __slots__ = ("header", "transactionID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    transactionID: _basic_types_pb2.TransactionID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., transactionID: _Optional[_Union[_basic_types_pb2.TransactionID, _Mapping]] = ...) -> None: ...

class TransactionGetFastRecordResponse(_message.Message):
    __slots__ = ("header", "transactionRecord")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONRECORD_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    transactionRecord: _transaction_record_pb2.TransactionRecord
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., transactionRecord: _Optional[_Union[_transaction_record_pb2.TransactionRecord, _Mapping]] = ...) -> None: ...
