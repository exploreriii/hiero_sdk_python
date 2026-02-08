from ... import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProofKeySet(_message.Message):
    __slots__ = ("adoption_time", "key", "next_key")
    ADOPTION_TIME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NEXT_KEY_FIELD_NUMBER: _ClassVar[int]
    adoption_time: _timestamp_pb2.Timestamp
    key: bytes
    next_key: bytes
    def __init__(self, adoption_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., key: _Optional[bytes] = ..., next_key: _Optional[bytes] = ...) -> None: ...

class ProofKey(_message.Message):
    __slots__ = ("node_id", "key")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    key: bytes
    def __init__(self, node_id: _Optional[int] = ..., key: _Optional[bytes] = ...) -> None: ...

class History(_message.Message):
    __slots__ = ("address_book_hash", "metadata")
    ADDRESS_BOOK_HASH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    address_book_hash: bytes
    metadata: bytes
    def __init__(self, address_book_hash: _Optional[bytes] = ..., metadata: _Optional[bytes] = ...) -> None: ...

class HistoryProof(_message.Message):
    __slots__ = ("source_address_book_hash", "target_proof_keys", "target_history", "proof")
    SOURCE_ADDRESS_BOOK_HASH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROOF_KEYS_FIELD_NUMBER: _ClassVar[int]
    TARGET_HISTORY_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    source_address_book_hash: bytes
    target_proof_keys: _containers.RepeatedCompositeFieldContainer[ProofKey]
    target_history: History
    proof: bytes
    def __init__(self, source_address_book_hash: _Optional[bytes] = ..., target_proof_keys: _Optional[_Iterable[_Union[ProofKey, _Mapping]]] = ..., target_history: _Optional[_Union[History, _Mapping]] = ..., proof: _Optional[bytes] = ...) -> None: ...

class HistoryProofConstruction(_message.Message):
    __slots__ = ("construction_id", "source_roster_hash", "source_proof", "target_roster_hash", "grace_period_end_time", "assembly_start_time", "target_proof", "failure_reason")
    CONSTRUCTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROOF_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_END_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSEMBLY_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROOF_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    construction_id: int
    source_roster_hash: bytes
    source_proof: HistoryProof
    target_roster_hash: bytes
    grace_period_end_time: _timestamp_pb2.Timestamp
    assembly_start_time: _timestamp_pb2.Timestamp
    target_proof: HistoryProof
    failure_reason: str
    def __init__(self, construction_id: _Optional[int] = ..., source_roster_hash: _Optional[bytes] = ..., source_proof: _Optional[_Union[HistoryProof, _Mapping]] = ..., target_roster_hash: _Optional[bytes] = ..., grace_period_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assembly_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target_proof: _Optional[_Union[HistoryProof, _Mapping]] = ..., failure_reason: _Optional[str] = ...) -> None: ...

class ConstructionNodeId(_message.Message):
    __slots__ = ("construction_id", "node_id")
    CONSTRUCTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    construction_id: int
    node_id: int
    def __init__(self, construction_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class HistoryProofVote(_message.Message):
    __slots__ = ("proof", "congruent_node_id")
    PROOF_FIELD_NUMBER: _ClassVar[int]
    CONGRUENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    proof: HistoryProof
    congruent_node_id: int
    def __init__(self, proof: _Optional[_Union[HistoryProof, _Mapping]] = ..., congruent_node_id: _Optional[int] = ...) -> None: ...

class HistorySignature(_message.Message):
    __slots__ = ("history", "signature")
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    history: History
    signature: bytes
    def __init__(self, history: _Optional[_Union[History, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class RecordedHistorySignature(_message.Message):
    __slots__ = ("signing_time", "history_signature")
    SIGNING_TIME_FIELD_NUMBER: _ClassVar[int]
    HISTORY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signing_time: _timestamp_pb2.Timestamp
    history_signature: HistorySignature
    def __init__(self, signing_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., history_signature: _Optional[_Union[HistorySignature, _Mapping]] = ...) -> None: ...
