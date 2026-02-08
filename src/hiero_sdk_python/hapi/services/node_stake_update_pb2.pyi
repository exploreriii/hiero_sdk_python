from . import basic_types_pb2 as _basic_types_pb2
from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeStakeUpdateTransactionBody(_message.Message):
    __slots__ = ("end_of_staking_period", "node_stake", "max_staking_reward_rate_per_hbar", "node_reward_fee_fraction", "staking_periods_stored", "staking_period", "staking_reward_fee_fraction", "staking_start_threshold", "staking_reward_rate", "reserved_staking_rewards", "unreserved_staking_reward_balance", "reward_balance_threshold", "max_stake_rewarded", "max_total_reward")
    END_OF_STAKING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    NODE_STAKE_FIELD_NUMBER: _ClassVar[int]
    MAX_STAKING_REWARD_RATE_PER_HBAR_FIELD_NUMBER: _ClassVar[int]
    NODE_REWARD_FEE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    STAKING_PERIODS_STORED_FIELD_NUMBER: _ClassVar[int]
    STAKING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FEE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    STAKING_START_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_RATE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_STAKING_REWARDS_FIELD_NUMBER: _ClassVar[int]
    UNRESERVED_STAKING_REWARD_BALANCE_FIELD_NUMBER: _ClassVar[int]
    REWARD_BALANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_STAKE_REWARDED_FIELD_NUMBER: _ClassVar[int]
    MAX_TOTAL_REWARD_FIELD_NUMBER: _ClassVar[int]
    end_of_staking_period: _timestamp_pb2.Timestamp
    node_stake: _containers.RepeatedCompositeFieldContainer[NodeStake]
    max_staking_reward_rate_per_hbar: int
    node_reward_fee_fraction: _basic_types_pb2.Fraction
    staking_periods_stored: int
    staking_period: int
    staking_reward_fee_fraction: _basic_types_pb2.Fraction
    staking_start_threshold: int
    staking_reward_rate: int
    reserved_staking_rewards: int
    unreserved_staking_reward_balance: int
    reward_balance_threshold: int
    max_stake_rewarded: int
    max_total_reward: int
    def __init__(self, end_of_staking_period: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., node_stake: _Optional[_Iterable[_Union[NodeStake, _Mapping]]] = ..., max_staking_reward_rate_per_hbar: _Optional[int] = ..., node_reward_fee_fraction: _Optional[_Union[_basic_types_pb2.Fraction, _Mapping]] = ..., staking_periods_stored: _Optional[int] = ..., staking_period: _Optional[int] = ..., staking_reward_fee_fraction: _Optional[_Union[_basic_types_pb2.Fraction, _Mapping]] = ..., staking_start_threshold: _Optional[int] = ..., staking_reward_rate: _Optional[int] = ..., reserved_staking_rewards: _Optional[int] = ..., unreserved_staking_reward_balance: _Optional[int] = ..., reward_balance_threshold: _Optional[int] = ..., max_stake_rewarded: _Optional[int] = ..., max_total_reward: _Optional[int] = ...) -> None: ...

class NodeStake(_message.Message):
    __slots__ = ("max_stake", "min_stake", "node_id", "reward_rate", "stake", "stake_not_rewarded", "stake_rewarded")
    MAX_STAKE_FIELD_NUMBER: _ClassVar[int]
    MIN_STAKE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_RATE_FIELD_NUMBER: _ClassVar[int]
    STAKE_FIELD_NUMBER: _ClassVar[int]
    STAKE_NOT_REWARDED_FIELD_NUMBER: _ClassVar[int]
    STAKE_REWARDED_FIELD_NUMBER: _ClassVar[int]
    max_stake: int
    min_stake: int
    node_id: int
    reward_rate: int
    stake: int
    stake_not_rewarded: int
    stake_rewarded: int
    def __init__(self, max_stake: _Optional[int] = ..., min_stake: _Optional[int] = ..., node_id: _Optional[int] = ..., reward_rate: _Optional[int] = ..., stake: _Optional[int] = ..., stake_not_rewarded: _Optional[int] = ..., stake_rewarded: _Optional[int] = ...) -> None: ...
