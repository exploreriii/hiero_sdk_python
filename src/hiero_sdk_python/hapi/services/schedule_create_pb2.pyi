from . import basic_types_pb2 as _basic_types_pb2
from . import timestamp_pb2 as _timestamp_pb2
from . import schedulable_transaction_body_pb2 as _schedulable_transaction_body_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleCreateTransactionBody(_message.Message):
    __slots__ = ("scheduledTransactionBody", "memo", "adminKey", "payerAccountID", "expiration_time", "wait_for_expiry")
    SCHEDULEDTRANSACTIONBODY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    ADMINKEY_FIELD_NUMBER: _ClassVar[int]
    PAYERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    scheduledTransactionBody: _schedulable_transaction_body_pb2.SchedulableTransactionBody
    memo: str
    adminKey: _basic_types_pb2.Key
    payerAccountID: _basic_types_pb2.AccountID
    expiration_time: _timestamp_pb2.Timestamp
    wait_for_expiry: bool
    def __init__(self, scheduledTransactionBody: _Optional[_Union[_schedulable_transaction_body_pb2.SchedulableTransactionBody, _Mapping]] = ..., memo: _Optional[str] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., payerAccountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., wait_for_expiry: bool = ...) -> None: ...
