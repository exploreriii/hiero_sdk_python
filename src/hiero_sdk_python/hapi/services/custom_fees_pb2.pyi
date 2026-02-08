from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FractionalFee(_message.Message):
    __slots__ = ("fractional_amount", "minimum_amount", "maximum_amount", "net_of_transfers")
    FRACTIONAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    NET_OF_TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    fractional_amount: _basic_types_pb2.Fraction
    minimum_amount: int
    maximum_amount: int
    net_of_transfers: bool
    def __init__(self, fractional_amount: _Optional[_Union[_basic_types_pb2.Fraction, _Mapping]] = ..., minimum_amount: _Optional[int] = ..., maximum_amount: _Optional[int] = ..., net_of_transfers: bool = ...) -> None: ...

class FixedFee(_message.Message):
    __slots__ = ("amount", "denominating_token_id")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DENOMINATING_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    denominating_token_id: _basic_types_pb2.TokenID
    def __init__(self, amount: _Optional[int] = ..., denominating_token_id: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ...) -> None: ...

class RoyaltyFee(_message.Message):
    __slots__ = ("exchange_value_fraction", "fallback_fee")
    EXCHANGE_VALUE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_FEE_FIELD_NUMBER: _ClassVar[int]
    exchange_value_fraction: _basic_types_pb2.Fraction
    fallback_fee: FixedFee
    def __init__(self, exchange_value_fraction: _Optional[_Union[_basic_types_pb2.Fraction, _Mapping]] = ..., fallback_fee: _Optional[_Union[FixedFee, _Mapping]] = ...) -> None: ...

class CustomFee(_message.Message):
    __slots__ = ("fixed_fee", "fractional_fee", "royalty_fee", "fee_collector_account_id", "all_collectors_are_exempt")
    FIXED_FEE_FIELD_NUMBER: _ClassVar[int]
    FRACTIONAL_FEE_FIELD_NUMBER: _ClassVar[int]
    ROYALTY_FEE_FIELD_NUMBER: _ClassVar[int]
    FEE_COLLECTOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_COLLECTORS_ARE_EXEMPT_FIELD_NUMBER: _ClassVar[int]
    fixed_fee: FixedFee
    fractional_fee: FractionalFee
    royalty_fee: RoyaltyFee
    fee_collector_account_id: _basic_types_pb2.AccountID
    all_collectors_are_exempt: bool
    def __init__(self, fixed_fee: _Optional[_Union[FixedFee, _Mapping]] = ..., fractional_fee: _Optional[_Union[FractionalFee, _Mapping]] = ..., royalty_fee: _Optional[_Union[RoyaltyFee, _Mapping]] = ..., fee_collector_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., all_collectors_are_exempt: bool = ...) -> None: ...

class AssessedCustomFee(_message.Message):
    __slots__ = ("amount", "token_id", "fee_collector_account_id", "effective_payer_account_id")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    FEE_COLLECTOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAYER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    token_id: _basic_types_pb2.TokenID
    fee_collector_account_id: _basic_types_pb2.AccountID
    effective_payer_account_id: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.AccountID]
    def __init__(self, amount: _Optional[int] = ..., token_id: _Optional[_Union[_basic_types_pb2.TokenID, _Mapping]] = ..., fee_collector_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., effective_payer_account_id: _Optional[_Iterable[_Union[_basic_types_pb2.AccountID, _Mapping]]] = ...) -> None: ...

class FixedCustomFee(_message.Message):
    __slots__ = ("fixed_fee", "fee_collector_account_id")
    FIXED_FEE_FIELD_NUMBER: _ClassVar[int]
    FEE_COLLECTOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    fixed_fee: FixedFee
    fee_collector_account_id: _basic_types_pb2.AccountID
    def __init__(self, fixed_fee: _Optional[_Union[FixedFee, _Mapping]] = ..., fee_collector_account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ...) -> None: ...

class FixedCustomFeeList(_message.Message):
    __slots__ = ("fees",)
    FEES_FIELD_NUMBER: _ClassVar[int]
    fees: _containers.RepeatedCompositeFieldContainer[FixedCustomFee]
    def __init__(self, fees: _Optional[_Iterable[_Union[FixedCustomFee, _Mapping]]] = ...) -> None: ...

class FeeExemptKeyList(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.Key]
    def __init__(self, keys: _Optional[_Iterable[_Union[_basic_types_pb2.Key, _Mapping]]] = ...) -> None: ...

class CustomFeeLimit(_message.Message):
    __slots__ = ("account_id", "fees")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    FEES_FIELD_NUMBER: _ClassVar[int]
    account_id: _basic_types_pb2.AccountID
    fees: _containers.RepeatedCompositeFieldContainer[FixedFee]
    def __init__(self, account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., fees: _Optional[_Iterable[_Union[FixedFee, _Mapping]]] = ...) -> None: ...
