from . import transaction_record_pb2 as _transaction_record_pb2
from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionGetRecordQuery(_message.Message):
    __slots__ = ("header", "transactionID", "includeDuplicates", "include_child_records")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    INCLUDEDUPLICATES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CHILD_RECORDS_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    transactionID: _basic_types_pb2.TransactionID
    includeDuplicates: bool
    include_child_records: bool
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., transactionID: _Optional[_Union[_basic_types_pb2.TransactionID, _Mapping]] = ..., includeDuplicates: bool = ..., include_child_records: bool = ...) -> None: ...

class TransactionGetRecordResponse(_message.Message):
    __slots__ = ("header", "transactionRecord", "duplicateTransactionRecords", "child_transaction_records")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONRECORD_FIELD_NUMBER: _ClassVar[int]
    DUPLICATETRANSACTIONRECORDS_FIELD_NUMBER: _ClassVar[int]
    CHILD_TRANSACTION_RECORDS_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    transactionRecord: _transaction_record_pb2.TransactionRecord
    duplicateTransactionRecords: _containers.RepeatedCompositeFieldContainer[_transaction_record_pb2.TransactionRecord]
    child_transaction_records: _containers.RepeatedCompositeFieldContainer[_transaction_record_pb2.TransactionRecord]
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., transactionRecord: _Optional[_Union[_transaction_record_pb2.TransactionRecord, _Mapping]] = ..., duplicateTransactionRecords: _Optional[_Iterable[_Union[_transaction_record_pb2.TransactionRecord, _Mapping]]] = ..., child_transaction_records: _Optional[_Iterable[_Union[_transaction_record_pb2.TransactionRecord, _Mapping]]] = ...) -> None: ...
