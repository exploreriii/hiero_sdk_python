from . import basic_types_pb2 as _basic_types_pb2
from . import transaction_record_pb2 as _transaction_record_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoGetAccountRecordsQuery(_message.Message):
    __slots__ = ("header", "accountID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    accountID: _basic_types_pb2.AccountID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class CryptoGetAccountRecordsResponse(_message.Message):
    __slots__ = ("header", "accountID", "records")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    accountID: _basic_types_pb2.AccountID
    records: _containers.RepeatedCompositeFieldContainer[_transaction_record_pb2.TransactionRecord]
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., records: _Optional[_Iterable[_Union[_transaction_record_pb2.TransactionRecord, _Mapping]]] = ...) -> None: ...
