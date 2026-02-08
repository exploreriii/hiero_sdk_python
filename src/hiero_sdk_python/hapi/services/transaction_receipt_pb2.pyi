from . import basic_types_pb2 as _basic_types_pb2
from . import response_code_pb2 as _response_code_pb2
from . import exchange_rate_pb2 as _exchange_rate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionReceipt(_message.Message):
    __slots__ = ("status", "accountID", "fileID", "contractID", "exchangeRate", "topicID", "topicSequenceNumber", "topicRunningHash", "topicRunningHashVersion", "tokenID", "newTotalSupply", "scheduleID", "scheduledTransactionID", "serialNumbers", "node_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGERATE_FIELD_NUMBER: _ClassVar[int]
    TOPICID_FIELD_NUMBER: _ClassVar[int]
    TOPICSEQUENCENUMBER_FIELD_NUMBER: _ClassVar[int]
    TOPICRUNNINGHASH_FIELD_NUMBER: _ClassVar[int]
    TOPICRUNNINGHASHVERSION_FIELD_NUMBER: _ClassVar[int]
    TOKENID_FIELD_NUMBER: _ClassVar[int]
    NEWTOTALSUPPLY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDTRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBERS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    status: _response_code_pb2.ResponseCodeEnum
    accountID: _basic_types_pb2.AccountID
    fileID: _basic_types_pb2.FileID
    contractID: _basic_types_pb2.ContractID
    exchangeRate: _exchange_rate_pb2.ExchangeRateSet
    topicID: _basic_types_pb2.TopicID
    topicSequenceNumber: int
    topicRunningHash: bytes
    topicRunningHashVersion: int
    tokenID: _basic_types_pb2.TokenID
    newTotalSupply: int
    scheduleID: _basic_types_pb2.ScheduleID
    scheduledTransactionID: _basic_types_pb2.TransactionID
    serialNumbers: _containers.RepeatedScalarFieldContainer[int]
    node_id: int
    def __init__(self, status: _Optional[_Union[_response_code_pb2.ResponseCodeEnum, str]] = ..., accountID: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., exchangeRate: _Optional[_Union[_exchange_rate_pb2.ExchangeRateSet, _Mapping]] = ..., topicID: _Optional[_Union[_basic_types_pb2.TopicID, _Mapping]] = ..., topicSequenceNumber: _Optional[int] = ..., topicRunningHash: _Optional[bytes] = ..., topicRunningHashVersion: _Optional[int] = ..., tokenID: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., newTotalSupply: _Optional[int] = ..., scheduleID: _Optional[_Union[_basic_types_pb2.ScheduleID, _Mapping]] = ..., scheduledTransactionID: _Optional[_Union[_basic_types_pb2.TransactionID, _Mapping]] = ..., serialNumbers: _Optional[_Iterable[int]] = ..., node_id: _Optional[int] = ...) -> None: ...
