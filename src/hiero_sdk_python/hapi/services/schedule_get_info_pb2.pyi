from . import basic_types_pb2 as _basic_types_pb2
from . import timestamp_pb2 as _timestamp_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from . import schedulable_transaction_body_pb2 as _schedulable_transaction_body_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleGetInfoQuery(_message.Message):
    __slots__ = ("header", "scheduleID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    scheduleID: _basic_types_pb2.ScheduleID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., scheduleID: _Optional[_Union[_basic_types_pb2.ScheduleID, _Mapping]] = ...) -> None: ...

class ScheduleInfo(_message.Message):
    __slots__ = ("scheduleID", "deletion_time", "execution_time", "expirationTime", "scheduledTransactionBody", "memo", "adminKey", "signers", "creatorAccountID", "payerAccountID", "scheduledTransactionID", "ledger_id", "wait_for_expiry")
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    DELETION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDTRANSACTIONBODY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    ADMINKEY_FIELD_NUMBER: _ClassVar[int]
    SIGNERS_FIELD_NUMBER: _ClassVar[int]
    CREATORACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    PAYERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDTRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    scheduleID: _basic_types_pb2.ScheduleID
    deletion_time: _timestamp_pb2.Timestamp
    execution_time: _timestamp_pb2.Timestamp
    expirationTime: _timestamp_pb2.Timestamp
    scheduledTransactionBody: _schedulable_transaction_body_pb2.SchedulableTransactionBody
    memo: str
    adminKey: _basic_types_pb2.Key
    signers: _basic_types_pb2.KeyList
    creatorAccountID: _basic_types_pb2.AccountID
    payerAccountID: _basic_types_pb2.AccountID
    scheduledTransactionID: _basic_types_pb2.TransactionID
    ledger_id: bytes
    wait_for_expiry: bool
    def __init__(self, scheduleID: _Optional[_Union[_basic_types_pb2.ScheduleID, _Mapping]] = ..., deletion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scheduledTransactionBody: _Optional[_Union[_schedulable_transaction_body_pb2.SchedulableTransactionBody, _Mapping]] = ..., memo: _Optional[str] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., signers: _Optional[_Union[_basic_types_pb2.KeyList, _Mapping]] = ..., creatorAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., payerAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., scheduledTransactionID: _Optional[_Union[_basic_types_pb2.TransactionID, _Mapping]] = ..., ledger_id: _Optional[bytes] = ..., wait_for_expiry: bool = ...) -> None: ...

class ScheduleGetInfoResponse(_message.Message):
    __slots__ = ("header", "scheduleInfo")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEINFO_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    scheduleInfo: ScheduleInfo
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., scheduleInfo: _Optional[_Union[ScheduleInfo, _Mapping]] = ...) -> None: ...
