from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InternalCallContext(_message.Message):
    __slots__ = ("gas", "value", "call_data")
    GAS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CALL_DATA_FIELD_NUMBER: _ClassVar[int]
    gas: int
    value: int
    call_data: bytes
    def __init__(self, gas: _Optional[int] = ..., value: _Optional[int] = ..., call_data: _Optional[bytes] = ...) -> None: ...

class EvmTransactionResult(_message.Message):
    __slots__ = ("sender_id", "contract_id", "result_data", "error_message", "gas_used", "internal_call_context")
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_CALL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    sender_id: _basic_types_pb2.AccountID
    contract_id: _basic_types_pb2.ContractID
    result_data: bytes
    error_message: str
    gas_used: int
    internal_call_context: InternalCallContext
    def __init__(self, sender_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., contract_id: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., result_data: _Optional[bytes] = ..., error_message: _Optional[str] = ..., gas_used: _Optional[int] = ..., internal_call_context: _Optional[_Union[InternalCallContext, _Mapping]] = ...) -> None: ...

class ContractNonceInfo(_message.Message):
    __slots__ = ("contract_id", "nonce")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    contract_id: _basic_types_pb2.ContractID
    nonce: int
    def __init__(self, contract_id: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., nonce: _Optional[int] = ...) -> None: ...

class ContractLoginfo(_message.Message):
    __slots__ = ("contractID", "bloom", "topic", "data")
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    BLOOM_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    contractID: _basic_types_pb2.ContractID
    bloom: bytes
    topic: _containers.RepeatedScalarFieldContainer[bytes]
    data: bytes
    def __init__(self, contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., bloom: _Optional[bytes] = ..., topic: _Optional[_Iterable[bytes]] = ..., data: _Optional[bytes] = ...) -> None: ...

class ContractFunctionResult(_message.Message):
    __slots__ = ("contractID", "contractCallResult", "errorMessage", "bloom", "gasUsed", "logInfo", "createdContractIDs", "evm_address", "gas", "amount", "functionParameters", "sender_id", "contract_nonces", "signer_nonce")
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTCALLRESULT_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    BLOOM_FIELD_NUMBER: _ClassVar[int]
    GASUSED_FIELD_NUMBER: _ClassVar[int]
    LOGINFO_FIELD_NUMBER: _ClassVar[int]
    CREATEDCONTRACTIDS_FIELD_NUMBER: _ClassVar[int]
    EVM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_NONCES_FIELD_NUMBER: _ClassVar[int]
    SIGNER_NONCE_FIELD_NUMBER: _ClassVar[int]
    contractID: _basic_types_pb2.ContractID
    contractCallResult: bytes
    errorMessage: str
    bloom: bytes
    gasUsed: int
    logInfo: _containers.RepeatedCompositeFieldContainer[ContractLoginfo]
    createdContractIDs: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.ContractID]
    evm_address: _wrappers_pb2.BytesValue
    gas: int
    amount: int
    functionParameters: bytes
    sender_id: _basic_types_pb2.AccountID
    contract_nonces: _containers.RepeatedCompositeFieldContainer[ContractNonceInfo]
    signer_nonce: _wrappers_pb2.Int64Value
    def __init__(self, contractID: _Optional[_Union[_basic_types_pb2.ContractID, _Mapping]] = ..., contractCallResult: _Optional[bytes] = ..., errorMessage: _Optional[str] = ..., bloom: _Optional[bytes] = ..., gasUsed: _Optional[int] = ..., logInfo: _Optional[_Iterable[_Union[ContractLoginfo, _Mapping]]] = ..., createdContractIDs: _Optional[_Iterable[_Union[_basic_types_pb2.ContractID, _Mapping]]] = ..., evm_address: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., gas: _Optional[int] = ..., amount: _Optional[int] = ..., functionParameters: _Optional[bytes] = ..., sender_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., contract_nonces: _Optional[_Iterable[_Union[ContractNonceInfo, _Mapping]]] = ..., signer_nonce: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
