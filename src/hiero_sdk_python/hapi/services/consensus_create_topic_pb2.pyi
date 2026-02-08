from . import basic_types_pb2 as _basic_types_pb2
from . import custom_fees_pb2 as _custom_fees_pb2
from . import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsensusCreateTopicTransactionBody(_message.Message):
    __slots__ = ("memo", "adminKey", "submitKey", "autoRenewPeriod", "autoRenewAccount", "fee_schedule_key", "fee_exempt_key_list", "custom_fees")
    MEMO_FIELD_NUMBER: _ClassVar[int]
    ADMINKEY_FIELD_NUMBER: _ClassVar[int]
    SUBMITKEY_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWPERIOD_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWACCOUNT_FIELD_NUMBER: _ClassVar[int]
    FEE_SCHEDULE_KEY_FIELD_NUMBER: _ClassVar[int]
    FEE_EXEMPT_KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEES_FIELD_NUMBER: _ClassVar[int]
    memo: str
    adminKey: _basic_types_pb2.Key
    submitKey: _basic_types_pb2.Key
    autoRenewPeriod: _duration_pb2.Duration
    autoRenewAccount: _basic_types_pb2.AccountID
    fee_schedule_key: _basic_types_pb2.Key
    fee_exempt_key_list: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.Key]
    custom_fees: _containers.RepeatedCompositeFieldContainer[_custom_fees_pb2.FixedCustomFee]
    def __init__(self, memo: _Optional[str] = ..., adminKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., submitKey: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., autoRenewPeriod: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., autoRenewAccount: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., fee_schedule_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., fee_exempt_key_list: _Optional[_Iterable[_Union[_basic_types_pb2.Key, _Mapping]]] = ..., custom_fees: _Optional[_Iterable[_Union[_custom_fees_pb2.FixedCustomFee, _Mapping]]] = ...) -> None: ...
