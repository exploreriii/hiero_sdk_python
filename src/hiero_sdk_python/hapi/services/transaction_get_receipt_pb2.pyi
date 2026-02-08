from . import transaction_receipt_pb2 as _transaction_receipt_pb2
from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionGetReceiptQuery(_message.Message):
    __slots__ = ("header", "transactionID", "includeDuplicates", "include_child_receipts")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    INCLUDEDUPLICATES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CHILD_RECEIPTS_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    transactionID: _basic_types_pb2.TransactionID
    includeDuplicates: bool
    include_child_receipts: bool
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., transactionID: _Optional[_Union[_basic_types_pb2.TransactionID, _Mapping]] = ..., includeDuplicates: bool = ..., include_child_receipts: bool = ...) -> None: ...

class TransactionGetReceiptResponse(_message.Message):
    __slots__ = ("header", "receipt", "duplicateTransactionReceipts", "child_transaction_receipts")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    DUPLICATETRANSACTIONRECEIPTS_FIELD_NUMBER: _ClassVar[int]
    CHILD_TRANSACTION_RECEIPTS_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    receipt: _transaction_receipt_pb2.TransactionReceipt
    duplicateTransactionReceipts: _containers.RepeatedCompositeFieldContainer[_transaction_receipt_pb2.TransactionReceipt]
    child_transaction_receipts: _containers.RepeatedCompositeFieldContainer[_transaction_receipt_pb2.TransactionReceipt]
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., receipt: _Optional[_Union[_transaction_receipt_pb2.TransactionReceipt, _Mapping]] = ..., duplicateTransactionReceipts: _Optional[_Iterable[_Union[_transaction_receipt_pb2.TransactionReceipt, _Mapping]]] = ..., child_transaction_receipts: _Optional[_Iterable[_Union[_transaction_receipt_pb2.TransactionReceipt, _Mapping]]] = ...) -> None: ...
