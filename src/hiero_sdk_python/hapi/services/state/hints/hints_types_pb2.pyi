from ... import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CRSStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATHERING_CONTRIBUTIONS: _ClassVar[CRSStage]
    WAITING_FOR_ADOPTING_FINAL_CRS: _ClassVar[CRSStage]
    COMPLETED: _ClassVar[CRSStage]
GATHERING_CONTRIBUTIONS: CRSStage
WAITING_FOR_ADOPTING_FINAL_CRS: CRSStage
COMPLETED: CRSStage

class HintsPartyId(_message.Message):
    __slots__ = ("party_id", "num_parties")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_PARTIES_FIELD_NUMBER: _ClassVar[int]
    party_id: int
    num_parties: int
    def __init__(self, party_id: _Optional[int] = ..., num_parties: _Optional[int] = ...) -> None: ...

class HintsKeySet(_message.Message):
    __slots__ = ("node_id", "adoption_time", "key", "next_key")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ADOPTION_TIME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NEXT_KEY_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    adoption_time: _timestamp_pb2.Timestamp
    key: bytes
    next_key: bytes
    def __init__(self, node_id: _Optional[int] = ..., adoption_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., key: _Optional[bytes] = ..., next_key: _Optional[bytes] = ...) -> None: ...

class PreprocessedKeys(_message.Message):
    __slots__ = ("aggregation_key", "verification_key")
    AGGREGATION_KEY_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    aggregation_key: bytes
    verification_key: bytes
    def __init__(self, aggregation_key: _Optional[bytes] = ..., verification_key: _Optional[bytes] = ...) -> None: ...

class PreprocessingVoteId(_message.Message):
    __slots__ = ("construction_id", "node_id")
    CONSTRUCTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    construction_id: int
    node_id: int
    def __init__(self, construction_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class PreprocessingVote(_message.Message):
    __slots__ = ("preprocessed_keys", "congruent_node_id")
    PREPROCESSED_KEYS_FIELD_NUMBER: _ClassVar[int]
    CONGRUENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    preprocessed_keys: PreprocessedKeys
    congruent_node_id: int
    def __init__(self, preprocessed_keys: _Optional[_Union[PreprocessedKeys, _Mapping]] = ..., congruent_node_id: _Optional[int] = ...) -> None: ...

class NodePartyId(_message.Message):
    __slots__ = ("node_id", "party_id", "party_weight")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    party_id: int
    party_weight: int
    def __init__(self, node_id: _Optional[int] = ..., party_id: _Optional[int] = ..., party_weight: _Optional[int] = ...) -> None: ...

class HintsScheme(_message.Message):
    __slots__ = ("preprocessed_keys", "node_party_ids")
    PREPROCESSED_KEYS_FIELD_NUMBER: _ClassVar[int]
    NODE_PARTY_IDS_FIELD_NUMBER: _ClassVar[int]
    preprocessed_keys: PreprocessedKeys
    node_party_ids: _containers.RepeatedCompositeFieldContainer[NodePartyId]
    def __init__(self, preprocessed_keys: _Optional[_Union[PreprocessedKeys, _Mapping]] = ..., node_party_ids: _Optional[_Iterable[_Union[NodePartyId, _Mapping]]] = ...) -> None: ...

class HintsConstruction(_message.Message):
    __slots__ = ("construction_id", "source_roster_hash", "target_roster_hash", "grace_period_end_time", "preprocessing_start_time", "hints_scheme")
    CONSTRUCTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_END_TIME_FIELD_NUMBER: _ClassVar[int]
    PREPROCESSING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    HINTS_SCHEME_FIELD_NUMBER: _ClassVar[int]
    construction_id: int
    source_roster_hash: bytes
    target_roster_hash: bytes
    grace_period_end_time: _timestamp_pb2.Timestamp
    preprocessing_start_time: _timestamp_pb2.Timestamp
    hints_scheme: HintsScheme
    def __init__(self, construction_id: _Optional[int] = ..., source_roster_hash: _Optional[bytes] = ..., target_roster_hash: _Optional[bytes] = ..., grace_period_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., preprocessing_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hints_scheme: _Optional[_Union[HintsScheme, _Mapping]] = ...) -> None: ...

class CRSState(_message.Message):
    __slots__ = ("crs", "stage", "next_contributing_node_id", "contribution_end_time")
    CRS_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    NEXT_CONTRIBUTING_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    crs: bytes
    stage: CRSStage
    next_contributing_node_id: _wrappers_pb2.UInt64Value
    contribution_end_time: _timestamp_pb2.Timestamp
    def __init__(self, crs: _Optional[bytes] = ..., stage: _Optional[_Union[CRSStage, str]] = ..., next_contributing_node_id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., contribution_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
