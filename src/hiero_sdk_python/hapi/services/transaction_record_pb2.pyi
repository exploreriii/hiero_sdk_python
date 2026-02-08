from . import timestamp_pb2 as _timestamp_pb2
from . import basic_types_pb2 as _basic_types_pb2
from . import custom_fees_pb2 as _custom_fees_pb2
from . import transaction_receipt_pb2 as _transaction_receipt_pb2
from . import contract_types_pb2 as _contract_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionRecord(_message.Message):
    __slots__ = ("receipt", "transactionHash", "consensusTimestamp", "transactionID", "memo", "transactionFee", "contractCallResult", "contractCreateResult", "transferList", "tokenTransferLists", "scheduleRef", "assessed_custom_fees", "automatic_token_associations", "parent_consensus_timestamp", "alias", "ethereum_hash", "paid_staking_rewards", "prng_bytes", "prng_number", "evm_address", "new_pending_airdrops")
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONHASH_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONFEE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTCALLRESULT_FIELD_NUMBER: _ClassVar[int]
    CONTRACTCREATERESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSFERLIST_FIELD_NUMBER: _ClassVar[int]
    TOKENTRANSFERLISTS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEREF_FIELD_NUMBER: _ClassVar[int]
    ASSESSED_CUSTOM_FEES_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_TOKEN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONSENSUS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    ETHEREUM_HASH_FIELD_NUMBER: _ClassVar[int]
    PAID_STAKING_REWARDS_FIELD_NUMBER: _ClassVar[int]
    PRNG_BYTES_FIELD_NUMBER: _ClassVar[int]
    PRNG_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EVM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NEW_PENDING_AIRDROPS_FIELD_NUMBER: _ClassVar[int]
    receipt: _transaction_receipt_pb2.TransactionReceipt
    transactionHash: bytes
    consensusTimestamp: _timestamp_pb2.Timestamp
    transactionID: _basic_types_pb2.TransactionID
    memo: str
    transactionFee: int
    contractCallResult: _contract_types_pb2.ContractFunctionResult
    contractCreateResult: _contract_types_pb2.ContractFunctionResult
    transferList: _basic_types_pb2.TransferList
    tokenTransferLists: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenTransferList]
    scheduleRef: _basic_types_pb2.ScheduleID
    assessed_custom_fees: _containers.RepeatedCompositeFieldContainer[_custom_fees_pb2.AssessedCustomFee]
    automatic_token_associations: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.TokenAssociation]
    parent_consensus_timestamp: _timestamp_pb2.Timestamp
    alias: bytes
    ethereum_hash: bytes
    paid_staking_rewards: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.AccountAmount]
    prng_bytes: bytes
    prng_number: int
    evm_address: bytes
    new_pending_airdrops: _containers.RepeatedCompositeFieldContainer[PendingAirdropRecord]
    def __init__(self, receipt: _Optional[_Union[_transaction_receipt_pb2.TransactionReceipt, _Mapping]] = ..., transactionHash: _Optional[bytes] = ..., consensusTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transactionID: _Optional[_Union[_basic_types_pb2.TransactionID, _Mapping]] = ..., memo: _Optional[str] = ..., transactionFee: _Optional[int] = ..., contractCallResult: _Optional[_Union[_contract_types_pb2.ContractFunctionResult, _Mapping]] = ..., contractCreateResult: _Optional[_Union[_contract_types_pb2.ContractFunctionResult, _Mapping]] = ..., transferList: _Optional[_Union[_basic_types_pb2.TransferList, _Mapping]] = ..., tokenTransferLists: _Optional[_Iterable[_Union[_basic_types_pb2.TokenTransferList, _Mapping]]] = ..., scheduleRef: _Optional[_Union[_basic_types_pb2.ScheduleID, _Mapping]] = ..., assessed_custom_fees: _Optional[_Iterable[_Union[_custom_fees_pb2.AssessedCustomFee, _Mapping]]] = ..., automatic_token_associations: _Optional[_Iterable[_Union[_basic_types_pb2.TokenAssociation, _Mapping]]] = ..., parent_consensus_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., alias: _Optional[bytes] = ..., ethereum_hash: _Optional[bytes] = ..., paid_staking_rewards: _Optional[_Iterable[_Union[_basic_types_pb2.AccountAmount, _Mapping]]] = ..., prng_bytes: _Optional[bytes] = ..., prng_number: _Optional[int] = ..., evm_address: _Optional[bytes] = ..., new_pending_airdrops: _Optional[_Iterable[_Union[PendingAirdropRecord, _Mapping]]] = ...) -> None: ...

class PendingAirdropRecord(_message.Message):
    __slots__ = ("pending_airdrop_id", "pending_airdrop_value")
    PENDING_AIRDROP_ID_FIELD_NUMBER: _ClassVar[int]
    PENDING_AIRDROP_VALUE_FIELD_NUMBER: _ClassVar[int]
    pending_airdrop_id: _basic_types_pb2.PendingAirdropId
    pending_airdrop_value: _basic_types_pb2.PendingAirdropValue
    def __init__(self, pending_airdrop_id: _Optional[_Union[_basic_types_pb2.PendingAirdropId, _Mapping]] = ..., pending_airdrop_value: _Optional[_Union[_basic_types_pb2.PendingAirdropValue, _Mapping]] = ...) -> None: ...
