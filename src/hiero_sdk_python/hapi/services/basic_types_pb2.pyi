from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockHashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHA2_384: _ClassVar[BlockHashAlgorithm]

class TokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUNGIBLE_COMMON: _ClassVar[TokenType]
    NON_FUNGIBLE_UNIQUE: _ClassVar[TokenType]

class SubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[SubType]
    TOKEN_FUNGIBLE_COMMON: _ClassVar[SubType]
    TOKEN_NON_FUNGIBLE_UNIQUE: _ClassVar[SubType]
    TOKEN_FUNGIBLE_COMMON_WITH_CUSTOM_FEES: _ClassVar[SubType]
    TOKEN_NON_FUNGIBLE_UNIQUE_WITH_CUSTOM_FEES: _ClassVar[SubType]
    SCHEDULE_CREATE_CONTRACT_CALL: _ClassVar[SubType]
    TOPIC_CREATE_WITH_CUSTOM_FEES: _ClassVar[SubType]
    SUBMIT_MESSAGE_WITH_CUSTOM_FEES: _ClassVar[SubType]

class TokenSupplyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFINITE: _ClassVar[TokenSupplyType]
    FINITE: _ClassVar[TokenSupplyType]

class TokenKeyValidation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FULL_VALIDATION: _ClassVar[TokenKeyValidation]
    NO_VALIDATION: _ClassVar[TokenKeyValidation]

class TokenFreezeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FreezeNotApplicable: _ClassVar[TokenFreezeStatus]
    Frozen: _ClassVar[TokenFreezeStatus]
    Unfrozen: _ClassVar[TokenFreezeStatus]

class TokenKycStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KycNotApplicable: _ClassVar[TokenKycStatus]
    Granted: _ClassVar[TokenKycStatus]
    Revoked: _ClassVar[TokenKycStatus]

class TokenPauseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PauseNotApplicable: _ClassVar[TokenPauseStatus]
    Paused: _ClassVar[TokenPauseStatus]
    Unpaused: _ClassVar[TokenPauseStatus]

class HederaFunctionality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[HederaFunctionality]
    CryptoTransfer: _ClassVar[HederaFunctionality]
    CryptoUpdate: _ClassVar[HederaFunctionality]
    CryptoDelete: _ClassVar[HederaFunctionality]
    CryptoAddLiveHash: _ClassVar[HederaFunctionality]
    CryptoDeleteLiveHash: _ClassVar[HederaFunctionality]
    ContractCall: _ClassVar[HederaFunctionality]
    ContractCreate: _ClassVar[HederaFunctionality]
    ContractUpdate: _ClassVar[HederaFunctionality]
    FileCreate: _ClassVar[HederaFunctionality]
    FileAppend: _ClassVar[HederaFunctionality]
    FileUpdate: _ClassVar[HederaFunctionality]
    FileDelete: _ClassVar[HederaFunctionality]
    CryptoGetAccountBalance: _ClassVar[HederaFunctionality]
    CryptoGetAccountRecords: _ClassVar[HederaFunctionality]
    CryptoGetInfo: _ClassVar[HederaFunctionality]
    ContractCallLocal: _ClassVar[HederaFunctionality]
    ContractGetInfo: _ClassVar[HederaFunctionality]
    ContractGetBytecode: _ClassVar[HederaFunctionality]
    GetBySolidityID: _ClassVar[HederaFunctionality]
    GetByKey: _ClassVar[HederaFunctionality]
    CryptoGetLiveHash: _ClassVar[HederaFunctionality]
    CryptoGetStakers: _ClassVar[HederaFunctionality]
    FileGetContents: _ClassVar[HederaFunctionality]
    FileGetInfo: _ClassVar[HederaFunctionality]
    TransactionGetRecord: _ClassVar[HederaFunctionality]
    ContractGetRecords: _ClassVar[HederaFunctionality]
    CryptoCreate: _ClassVar[HederaFunctionality]
    SystemDelete: _ClassVar[HederaFunctionality]
    SystemUndelete: _ClassVar[HederaFunctionality]
    ContractDelete: _ClassVar[HederaFunctionality]
    Freeze: _ClassVar[HederaFunctionality]
    CreateTransactionRecord: _ClassVar[HederaFunctionality]
    CryptoAccountAutoRenew: _ClassVar[HederaFunctionality]
    ContractAutoRenew: _ClassVar[HederaFunctionality]
    GetVersionInfo: _ClassVar[HederaFunctionality]
    TransactionGetReceipt: _ClassVar[HederaFunctionality]
    ConsensusCreateTopic: _ClassVar[HederaFunctionality]
    ConsensusUpdateTopic: _ClassVar[HederaFunctionality]
    ConsensusDeleteTopic: _ClassVar[HederaFunctionality]
    ConsensusGetTopicInfo: _ClassVar[HederaFunctionality]
    ConsensusSubmitMessage: _ClassVar[HederaFunctionality]
    UncheckedSubmit: _ClassVar[HederaFunctionality]
    TokenCreate: _ClassVar[HederaFunctionality]
    TokenGetInfo: _ClassVar[HederaFunctionality]
    TokenFreezeAccount: _ClassVar[HederaFunctionality]
    TokenUnfreezeAccount: _ClassVar[HederaFunctionality]
    TokenGrantKycToAccount: _ClassVar[HederaFunctionality]
    TokenRevokeKycFromAccount: _ClassVar[HederaFunctionality]
    TokenDelete: _ClassVar[HederaFunctionality]
    TokenUpdate: _ClassVar[HederaFunctionality]
    TokenMint: _ClassVar[HederaFunctionality]
    TokenBurn: _ClassVar[HederaFunctionality]
    TokenAccountWipe: _ClassVar[HederaFunctionality]
    TokenAssociateToAccount: _ClassVar[HederaFunctionality]
    TokenDissociateFromAccount: _ClassVar[HederaFunctionality]
    ScheduleCreate: _ClassVar[HederaFunctionality]
    ScheduleDelete: _ClassVar[HederaFunctionality]
    ScheduleSign: _ClassVar[HederaFunctionality]
    ScheduleGetInfo: _ClassVar[HederaFunctionality]
    TokenGetAccountNftInfos: _ClassVar[HederaFunctionality]
    TokenGetNftInfo: _ClassVar[HederaFunctionality]
    TokenGetNftInfos: _ClassVar[HederaFunctionality]
    TokenFeeScheduleUpdate: _ClassVar[HederaFunctionality]
    NetworkGetExecutionTime: _ClassVar[HederaFunctionality]
    TokenPause: _ClassVar[HederaFunctionality]
    TokenUnpause: _ClassVar[HederaFunctionality]
    CryptoApproveAllowance: _ClassVar[HederaFunctionality]
    CryptoDeleteAllowance: _ClassVar[HederaFunctionality]
    GetAccountDetails: _ClassVar[HederaFunctionality]
    EthereumTransaction: _ClassVar[HederaFunctionality]
    NodeStakeUpdate: _ClassVar[HederaFunctionality]
    UtilPrng: _ClassVar[HederaFunctionality]
    TransactionGetFastRecord: _ClassVar[HederaFunctionality]
    TokenUpdateNfts: _ClassVar[HederaFunctionality]
    NodeCreate: _ClassVar[HederaFunctionality]
    NodeUpdate: _ClassVar[HederaFunctionality]
    NodeDelete: _ClassVar[HederaFunctionality]
    TokenReject: _ClassVar[HederaFunctionality]
    TokenAirdrop: _ClassVar[HederaFunctionality]
    TokenCancelAirdrop: _ClassVar[HederaFunctionality]
    TokenClaimAirdrop: _ClassVar[HederaFunctionality]
    StateSignatureTransaction: _ClassVar[HederaFunctionality]
    HintsKeyPublication: _ClassVar[HederaFunctionality]
    HintsPreprocessingVote: _ClassVar[HederaFunctionality]
    HintsPartialSignature: _ClassVar[HederaFunctionality]
    HistoryAssemblySignature: _ClassVar[HederaFunctionality]
    HistoryProofKeyPublication: _ClassVar[HederaFunctionality]
    HistoryProofVote: _ClassVar[HederaFunctionality]
    CrsPublication: _ClassVar[HederaFunctionality]
    AtomicBatch: _ClassVar[HederaFunctionality]
    LambdaSStore: _ClassVar[HederaFunctionality]
    HookDispatch: _ClassVar[HederaFunctionality]
SHA2_384: BlockHashAlgorithm
FUNGIBLE_COMMON: TokenType
NON_FUNGIBLE_UNIQUE: TokenType
DEFAULT: SubType
TOKEN_FUNGIBLE_COMMON: SubType
TOKEN_NON_FUNGIBLE_UNIQUE: SubType
TOKEN_FUNGIBLE_COMMON_WITH_CUSTOM_FEES: SubType
TOKEN_NON_FUNGIBLE_UNIQUE_WITH_CUSTOM_FEES: SubType
SCHEDULE_CREATE_CONTRACT_CALL: SubType
TOPIC_CREATE_WITH_CUSTOM_FEES: SubType
SUBMIT_MESSAGE_WITH_CUSTOM_FEES: SubType
INFINITE: TokenSupplyType
FINITE: TokenSupplyType
FULL_VALIDATION: TokenKeyValidation
NO_VALIDATION: TokenKeyValidation
FreezeNotApplicable: TokenFreezeStatus
Frozen: TokenFreezeStatus
Unfrozen: TokenFreezeStatus
KycNotApplicable: TokenKycStatus
Granted: TokenKycStatus
Revoked: TokenKycStatus
PauseNotApplicable: TokenPauseStatus
Paused: TokenPauseStatus
Unpaused: TokenPauseStatus
NONE: HederaFunctionality
CryptoTransfer: HederaFunctionality
CryptoUpdate: HederaFunctionality
CryptoDelete: HederaFunctionality
CryptoAddLiveHash: HederaFunctionality
CryptoDeleteLiveHash: HederaFunctionality
ContractCall: HederaFunctionality
ContractCreate: HederaFunctionality
ContractUpdate: HederaFunctionality
FileCreate: HederaFunctionality
FileAppend: HederaFunctionality
FileUpdate: HederaFunctionality
FileDelete: HederaFunctionality
CryptoGetAccountBalance: HederaFunctionality
CryptoGetAccountRecords: HederaFunctionality
CryptoGetInfo: HederaFunctionality
ContractCallLocal: HederaFunctionality
ContractGetInfo: HederaFunctionality
ContractGetBytecode: HederaFunctionality
GetBySolidityID: HederaFunctionality
GetByKey: HederaFunctionality
CryptoGetLiveHash: HederaFunctionality
CryptoGetStakers: HederaFunctionality
FileGetContents: HederaFunctionality
FileGetInfo: HederaFunctionality
TransactionGetRecord: HederaFunctionality
ContractGetRecords: HederaFunctionality
CryptoCreate: HederaFunctionality
SystemDelete: HederaFunctionality
SystemUndelete: HederaFunctionality
ContractDelete: HederaFunctionality
Freeze: HederaFunctionality
CreateTransactionRecord: HederaFunctionality
CryptoAccountAutoRenew: HederaFunctionality
ContractAutoRenew: HederaFunctionality
GetVersionInfo: HederaFunctionality
TransactionGetReceipt: HederaFunctionality
ConsensusCreateTopic: HederaFunctionality
ConsensusUpdateTopic: HederaFunctionality
ConsensusDeleteTopic: HederaFunctionality
ConsensusGetTopicInfo: HederaFunctionality
ConsensusSubmitMessage: HederaFunctionality
UncheckedSubmit: HederaFunctionality
TokenCreate: HederaFunctionality
TokenGetInfo: HederaFunctionality
TokenFreezeAccount: HederaFunctionality
TokenUnfreezeAccount: HederaFunctionality
TokenGrantKycToAccount: HederaFunctionality
TokenRevokeKycFromAccount: HederaFunctionality
TokenDelete: HederaFunctionality
TokenUpdate: HederaFunctionality
TokenMint: HederaFunctionality
TokenBurn: HederaFunctionality
TokenAccountWipe: HederaFunctionality
TokenAssociateToAccount: HederaFunctionality
TokenDissociateFromAccount: HederaFunctionality
ScheduleCreate: HederaFunctionality
ScheduleDelete: HederaFunctionality
ScheduleSign: HederaFunctionality
ScheduleGetInfo: HederaFunctionality
TokenGetAccountNftInfos: HederaFunctionality
TokenGetNftInfo: HederaFunctionality
TokenGetNftInfos: HederaFunctionality
TokenFeeScheduleUpdate: HederaFunctionality
NetworkGetExecutionTime: HederaFunctionality
TokenPause: HederaFunctionality
TokenUnpause: HederaFunctionality
CryptoApproveAllowance: HederaFunctionality
CryptoDeleteAllowance: HederaFunctionality
GetAccountDetails: HederaFunctionality
EthereumTransaction: HederaFunctionality
NodeStakeUpdate: HederaFunctionality
UtilPrng: HederaFunctionality
TransactionGetFastRecord: HederaFunctionality
TokenUpdateNfts: HederaFunctionality
NodeCreate: HederaFunctionality
NodeUpdate: HederaFunctionality
NodeDelete: HederaFunctionality
TokenReject: HederaFunctionality
TokenAirdrop: HederaFunctionality
TokenCancelAirdrop: HederaFunctionality
TokenClaimAirdrop: HederaFunctionality
StateSignatureTransaction: HederaFunctionality
HintsKeyPublication: HederaFunctionality
HintsPreprocessingVote: HederaFunctionality
HintsPartialSignature: HederaFunctionality
HistoryAssemblySignature: HederaFunctionality
HistoryProofKeyPublication: HederaFunctionality
HistoryProofVote: HederaFunctionality
CrsPublication: HederaFunctionality
AtomicBatch: HederaFunctionality
LambdaSStore: HederaFunctionality
HookDispatch: HederaFunctionality

class ShardID(_message.Message):
    __slots__ = ("shardNum",)
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    def __init__(self, shardNum: _Optional[int] = ...) -> None: ...

class RealmID(_message.Message):
    __slots__ = ("shardNum", "realmNum")
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    REALMNUM_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    realmNum: int
    def __init__(self, shardNum: _Optional[int] = ..., realmNum: _Optional[int] = ...) -> None: ...

class TokenID(_message.Message):
    __slots__ = ("shardNum", "realmNum", "tokenNum")
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    REALMNUM_FIELD_NUMBER: _ClassVar[int]
    TOKENNUM_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    realmNum: int
    tokenNum: int
    def __init__(self, shardNum: _Optional[int] = ..., realmNum: _Optional[int] = ..., tokenNum: _Optional[int] = ...) -> None: ...

class AccountID(_message.Message):
    __slots__ = ("shardNum", "realmNum", "accountNum", "alias")
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    REALMNUM_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUM_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    realmNum: int
    accountNum: int
    alias: bytes
    def __init__(self, shardNum: _Optional[int] = ..., realmNum: _Optional[int] = ..., accountNum: _Optional[int] = ..., alias: _Optional[bytes] = ...) -> None: ...

class NftID(_message.Message):
    __slots__ = ("token_ID", "serial_number")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    token_ID: TokenID
    serial_number: int
    def __init__(self, token_ID: _Optional[_Union[TokenID, _Mapping]] = ..., serial_number: _Optional[int] = ...) -> None: ...

class FileID(_message.Message):
    __slots__ = ("shardNum", "realmNum", "fileNum")
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    REALMNUM_FIELD_NUMBER: _ClassVar[int]
    FILENUM_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    realmNum: int
    fileNum: int
    def __init__(self, shardNum: _Optional[int] = ..., realmNum: _Optional[int] = ..., fileNum: _Optional[int] = ...) -> None: ...

class ContractID(_message.Message):
    __slots__ = ("shardNum", "realmNum", "contractNum", "evm_address")
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    REALMNUM_FIELD_NUMBER: _ClassVar[int]
    CONTRACTNUM_FIELD_NUMBER: _ClassVar[int]
    EVM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    realmNum: int
    contractNum: int
    evm_address: bytes
    def __init__(self, shardNum: _Optional[int] = ..., realmNum: _Optional[int] = ..., contractNum: _Optional[int] = ..., evm_address: _Optional[bytes] = ...) -> None: ...

class TopicID(_message.Message):
    __slots__ = ("shardNum", "realmNum", "topicNum")
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    REALMNUM_FIELD_NUMBER: _ClassVar[int]
    TOPICNUM_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    realmNum: int
    topicNum: int
    def __init__(self, shardNum: _Optional[int] = ..., realmNum: _Optional[int] = ..., topicNum: _Optional[int] = ...) -> None: ...

class ScheduleID(_message.Message):
    __slots__ = ("shardNum", "realmNum", "scheduleNum")
    SHARDNUM_FIELD_NUMBER: _ClassVar[int]
    REALMNUM_FIELD_NUMBER: _ClassVar[int]
    SCHEDULENUM_FIELD_NUMBER: _ClassVar[int]
    shardNum: int
    realmNum: int
    scheduleNum: int
    def __init__(self, shardNum: _Optional[int] = ..., realmNum: _Optional[int] = ..., scheduleNum: _Optional[int] = ...) -> None: ...

class TransactionID(_message.Message):
    __slots__ = ("transactionValidStart", "accountID", "scheduled", "nonce")
    TRANSACTIONVALIDSTART_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    transactionValidStart: _timestamp_pb2.Timestamp
    accountID: AccountID
    scheduled: bool
    nonce: int
    def __init__(self, transactionValidStart: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., accountID: _Optional[_Union[AccountID, _Mapping]] = ..., scheduled: bool = ..., nonce: _Optional[int] = ...) -> None: ...

class HookId(_message.Message):
    __slots__ = ("entity_id", "hook_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: HookEntityId
    hook_id: int
    def __init__(self, entity_id: _Optional[_Union[HookEntityId, _Mapping]] = ..., hook_id: _Optional[int] = ...) -> None: ...

class HookEntityId(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: AccountID
    def __init__(self, account_id: _Optional[_Union[AccountID, _Mapping]] = ...) -> None: ...

class HookCall(_message.Message):
    __slots__ = ("full_hook_id", "hook_id", "evm_hook_call")
    FULL_HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    EVM_HOOK_CALL_FIELD_NUMBER: _ClassVar[int]
    full_hook_id: HookId
    hook_id: int
    evm_hook_call: EvmHookCall
    def __init__(self, full_hook_id: _Optional[_Union[HookId, _Mapping]] = ..., hook_id: _Optional[int] = ..., evm_hook_call: _Optional[_Union[EvmHookCall, _Mapping]] = ...) -> None: ...

class EvmHookCall(_message.Message):
    __slots__ = ("data", "gas_limit")
    DATA_FIELD_NUMBER: _ClassVar[int]
    GAS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    gas_limit: int
    def __init__(self, data: _Optional[bytes] = ..., gas_limit: _Optional[int] = ...) -> None: ...

class AccountAmount(_message.Message):
    __slots__ = ("accountID", "amount", "is_approval", "pre_tx_allowance_hook", "pre_post_tx_allowance_hook")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    PRE_TX_ALLOWANCE_HOOK_FIELD_NUMBER: _ClassVar[int]
    PRE_POST_TX_ALLOWANCE_HOOK_FIELD_NUMBER: _ClassVar[int]
    accountID: AccountID
    amount: int
    is_approval: bool
    pre_tx_allowance_hook: HookCall
    pre_post_tx_allowance_hook: HookCall
    def __init__(self, accountID: _Optional[_Union[AccountID, _Mapping]] = ..., amount: _Optional[int] = ..., is_approval: bool = ..., pre_tx_allowance_hook: _Optional[_Union[HookCall, _Mapping]] = ..., pre_post_tx_allowance_hook: _Optional[_Union[HookCall, _Mapping]] = ...) -> None: ...

class TransferList(_message.Message):
    __slots__ = ("accountAmounts",)
    ACCOUNTAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    accountAmounts: _containers.RepeatedCompositeFieldContainer[AccountAmount]
    def __init__(self, accountAmounts: _Optional[_Iterable[_Union[AccountAmount, _Mapping]]] = ...) -> None: ...

class NftTransfer(_message.Message):
    __slots__ = ("senderAccountID", "receiverAccountID", "serialNumber", "is_approval", "pre_tx_sender_allowance_hook", "pre_post_tx_sender_allowance_hook", "pre_tx_receiver_allowance_hook", "pre_post_tx_receiver_allowance_hook")
    SENDERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    RECEIVERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    IS_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    PRE_TX_SENDER_ALLOWANCE_HOOK_FIELD_NUMBER: _ClassVar[int]
    PRE_POST_TX_SENDER_ALLOWANCE_HOOK_FIELD_NUMBER: _ClassVar[int]
    PRE_TX_RECEIVER_ALLOWANCE_HOOK_FIELD_NUMBER: _ClassVar[int]
    PRE_POST_TX_RECEIVER_ALLOWANCE_HOOK_FIELD_NUMBER: _ClassVar[int]
    senderAccountID: AccountID
    receiverAccountID: AccountID
    serialNumber: int
    is_approval: bool
    pre_tx_sender_allowance_hook: HookCall
    pre_post_tx_sender_allowance_hook: HookCall
    pre_tx_receiver_allowance_hook: HookCall
    pre_post_tx_receiver_allowance_hook: HookCall
    def __init__(self, senderAccountID: _Optional[_Union[AccountID, _Mapping]] = ..., receiverAccountID: _Optional[_Union[AccountID, _Mapping]] = ..., serialNumber: _Optional[int] = ..., is_approval: bool = ..., pre_tx_sender_allowance_hook: _Optional[_Union[HookCall, _Mapping]] = ..., pre_post_tx_sender_allowance_hook: _Optional[_Union[HookCall, _Mapping]] = ..., pre_tx_receiver_allowance_hook: _Optional[_Union[HookCall, _Mapping]] = ..., pre_post_tx_receiver_allowance_hook: _Optional[_Union[HookCall, _Mapping]] = ...) -> None: ...

class TokenTransferList(_message.Message):
    __slots__ = ("token", "transfers", "nftTransfers", "expected_decimals")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    NFTTRANSFERS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DECIMALS_FIELD_NUMBER: _ClassVar[int]
    token: TokenID
    transfers: _containers.RepeatedCompositeFieldContainer[AccountAmount]
    nftTransfers: _containers.RepeatedCompositeFieldContainer[NftTransfer]
    expected_decimals: _wrappers_pb2.UInt32Value
    def __init__(self, token: _Optional[_Union[TokenID, _Mapping]] = ..., transfers: _Optional[_Iterable[_Union[AccountAmount, _Mapping]]] = ..., nftTransfers: _Optional[_Iterable[_Union[NftTransfer, _Mapping]]] = ..., expected_decimals: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class Fraction(_message.Message):
    __slots__ = ("numerator", "denominator")
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    numerator: int
    denominator: int
    def __init__(self, numerator: _Optional[int] = ..., denominator: _Optional[int] = ...) -> None: ...

class Key(_message.Message):
    __slots__ = ("contractID", "ed25519", "RSA_3072", "ECDSA_384", "thresholdKey", "keyList", "ECDSA_secp256k1", "delegatable_contract_id")
    CONTRACTID_FIELD_NUMBER: _ClassVar[int]
    ED25519_FIELD_NUMBER: _ClassVar[int]
    RSA_3072_FIELD_NUMBER: _ClassVar[int]
    ECDSA_384_FIELD_NUMBER: _ClassVar[int]
    THRESHOLDKEY_FIELD_NUMBER: _ClassVar[int]
    KEYLIST_FIELD_NUMBER: _ClassVar[int]
    ECDSA_SECP256K1_FIELD_NUMBER: _ClassVar[int]
    DELEGATABLE_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    contractID: ContractID
    ed25519: bytes
    RSA_3072: bytes
    ECDSA_384: bytes
    thresholdKey: ThresholdKey
    keyList: KeyList
    ECDSA_secp256k1: bytes
    delegatable_contract_id: ContractID
    def __init__(self, contractID: _Optional[_Union[ContractID, _Mapping]] = ..., ed25519: _Optional[bytes] = ..., RSA_3072: _Optional[bytes] = ..., ECDSA_384: _Optional[bytes] = ..., thresholdKey: _Optional[_Union[ThresholdKey, _Mapping]] = ..., keyList: _Optional[_Union[KeyList, _Mapping]] = ..., ECDSA_secp256k1: _Optional[bytes] = ..., delegatable_contract_id: _Optional[_Union[ContractID, _Mapping]] = ...) -> None: ...

class ThresholdKey(_message.Message):
    __slots__ = ("threshold", "keys")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    keys: KeyList
    def __init__(self, threshold: _Optional[int] = ..., keys: _Optional[_Union[KeyList, _Mapping]] = ...) -> None: ...

class KeyList(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[Key]
    def __init__(self, keys: _Optional[_Iterable[_Union[Key, _Mapping]]] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ("contract", "ed25519", "RSA_3072", "ECDSA_384", "thresholdSignature", "signatureList")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ED25519_FIELD_NUMBER: _ClassVar[int]
    RSA_3072_FIELD_NUMBER: _ClassVar[int]
    ECDSA_384_FIELD_NUMBER: _ClassVar[int]
    THRESHOLDSIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURELIST_FIELD_NUMBER: _ClassVar[int]
    contract: bytes
    ed25519: bytes
    RSA_3072: bytes
    ECDSA_384: bytes
    thresholdSignature: ThresholdSignature
    signatureList: SignatureList
    def __init__(self, contract: _Optional[bytes] = ..., ed25519: _Optional[bytes] = ..., RSA_3072: _Optional[bytes] = ..., ECDSA_384: _Optional[bytes] = ..., thresholdSignature: _Optional[_Union[ThresholdSignature, _Mapping]] = ..., signatureList: _Optional[_Union[SignatureList, _Mapping]] = ...) -> None: ...

class ThresholdSignature(_message.Message):
    __slots__ = ("sigs",)
    SIGS_FIELD_NUMBER: _ClassVar[int]
    sigs: SignatureList
    def __init__(self, sigs: _Optional[_Union[SignatureList, _Mapping]] = ...) -> None: ...

class SignatureList(_message.Message):
    __slots__ = ("sigs",)
    SIGS_FIELD_NUMBER: _ClassVar[int]
    sigs: _containers.RepeatedCompositeFieldContainer[Signature]
    def __init__(self, sigs: _Optional[_Iterable[_Union[Signature, _Mapping]]] = ...) -> None: ...

class SignaturePair(_message.Message):
    __slots__ = ("pubKeyPrefix", "contract", "ed25519", "RSA_3072", "ECDSA_384", "ECDSA_secp256k1")
    PUBKEYPREFIX_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ED25519_FIELD_NUMBER: _ClassVar[int]
    RSA_3072_FIELD_NUMBER: _ClassVar[int]
    ECDSA_384_FIELD_NUMBER: _ClassVar[int]
    ECDSA_SECP256K1_FIELD_NUMBER: _ClassVar[int]
    pubKeyPrefix: bytes
    contract: bytes
    ed25519: bytes
    RSA_3072: bytes
    ECDSA_384: bytes
    ECDSA_secp256k1: bytes
    def __init__(self, pubKeyPrefix: _Optional[bytes] = ..., contract: _Optional[bytes] = ..., ed25519: _Optional[bytes] = ..., RSA_3072: _Optional[bytes] = ..., ECDSA_384: _Optional[bytes] = ..., ECDSA_secp256k1: _Optional[bytes] = ...) -> None: ...

class SignatureMap(_message.Message):
    __slots__ = ("sigPair",)
    SIGPAIR_FIELD_NUMBER: _ClassVar[int]
    sigPair: _containers.RepeatedCompositeFieldContainer[SignaturePair]
    def __init__(self, sigPair: _Optional[_Iterable[_Union[SignaturePair, _Mapping]]] = ...) -> None: ...

class FeeComponents(_message.Message):
    __slots__ = ("min", "max", "constant", "bpt", "vpt", "rbh", "sbh", "gas", "tv", "bpr", "sbpr")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    BPT_FIELD_NUMBER: _ClassVar[int]
    VPT_FIELD_NUMBER: _ClassVar[int]
    RBH_FIELD_NUMBER: _ClassVar[int]
    SBH_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    TV_FIELD_NUMBER: _ClassVar[int]
    BPR_FIELD_NUMBER: _ClassVar[int]
    SBPR_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int
    constant: int
    bpt: int
    vpt: int
    rbh: int
    sbh: int
    gas: int
    tv: int
    bpr: int
    sbpr: int
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ..., constant: _Optional[int] = ..., bpt: _Optional[int] = ..., vpt: _Optional[int] = ..., rbh: _Optional[int] = ..., sbh: _Optional[int] = ..., gas: _Optional[int] = ..., tv: _Optional[int] = ..., bpr: _Optional[int] = ..., sbpr: _Optional[int] = ...) -> None: ...

class TransactionFeeSchedule(_message.Message):
    __slots__ = ("hederaFunctionality", "feeData", "fees")
    HEDERAFUNCTIONALITY_FIELD_NUMBER: _ClassVar[int]
    FEEDATA_FIELD_NUMBER: _ClassVar[int]
    FEES_FIELD_NUMBER: _ClassVar[int]
    hederaFunctionality: HederaFunctionality
    feeData: FeeData
    fees: _containers.RepeatedCompositeFieldContainer[FeeData]
    def __init__(self, hederaFunctionality: _Optional[_Union[HederaFunctionality, str]] = ..., feeData: _Optional[_Union[FeeData, _Mapping]] = ..., fees: _Optional[_Iterable[_Union[FeeData, _Mapping]]] = ...) -> None: ...

class FeeData(_message.Message):
    __slots__ = ("nodedata", "networkdata", "servicedata", "subType")
    NODEDATA_FIELD_NUMBER: _ClassVar[int]
    NETWORKDATA_FIELD_NUMBER: _ClassVar[int]
    SERVICEDATA_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    nodedata: FeeComponents
    networkdata: FeeComponents
    servicedata: FeeComponents
    subType: SubType
    def __init__(self, nodedata: _Optional[_Union[FeeComponents, _Mapping]] = ..., networkdata: _Optional[_Union[FeeComponents, _Mapping]] = ..., servicedata: _Optional[_Union[FeeComponents, _Mapping]] = ..., subType: _Optional[_Union[SubType, str]] = ...) -> None: ...

class FeeSchedule(_message.Message):
    __slots__ = ("transactionFeeSchedule", "expiryTime")
    TRANSACTIONFEESCHEDULE_FIELD_NUMBER: _ClassVar[int]
    EXPIRYTIME_FIELD_NUMBER: _ClassVar[int]
    transactionFeeSchedule: _containers.RepeatedCompositeFieldContainer[TransactionFeeSchedule]
    expiryTime: _timestamp_pb2.TimestampSeconds
    def __init__(self, transactionFeeSchedule: _Optional[_Iterable[_Union[TransactionFeeSchedule, _Mapping]]] = ..., expiryTime: _Optional[_Union[_timestamp_pb2.TimestampSeconds, _Mapping]] = ...) -> None: ...

class CurrentAndNextFeeSchedule(_message.Message):
    __slots__ = ("currentFeeSchedule", "nextFeeSchedule")
    CURRENTFEESCHEDULE_FIELD_NUMBER: _ClassVar[int]
    NEXTFEESCHEDULE_FIELD_NUMBER: _ClassVar[int]
    currentFeeSchedule: FeeSchedule
    nextFeeSchedule: FeeSchedule
    def __init__(self, currentFeeSchedule: _Optional[_Union[FeeSchedule, _Mapping]] = ..., nextFeeSchedule: _Optional[_Union[FeeSchedule, _Mapping]] = ...) -> None: ...

class ServiceEndpoint(_message.Message):
    __slots__ = ("ipAddressV4", "port", "domain_name")
    IPADDRESSV4_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ipAddressV4: bytes
    port: int
    domain_name: str
    def __init__(self, ipAddressV4: _Optional[bytes] = ..., port: _Optional[int] = ..., domain_name: _Optional[str] = ...) -> None: ...

class NodeAddress(_message.Message):
    __slots__ = ("ipAddress", "portno", "memo", "RSA_PubKey", "nodeId", "nodeAccountId", "nodeCertHash", "serviceEndpoint", "description", "stake")
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORTNO_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    RSA_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    NODEACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    NODECERTHASH_FIELD_NUMBER: _ClassVar[int]
    SERVICEENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STAKE_FIELD_NUMBER: _ClassVar[int]
    ipAddress: bytes
    portno: int
    memo: bytes
    RSA_PubKey: str
    nodeId: int
    nodeAccountId: AccountID
    nodeCertHash: bytes
    serviceEndpoint: _containers.RepeatedCompositeFieldContainer[ServiceEndpoint]
    description: str
    stake: int
    def __init__(self, ipAddress: _Optional[bytes] = ..., portno: _Optional[int] = ..., memo: _Optional[bytes] = ..., RSA_PubKey: _Optional[str] = ..., nodeId: _Optional[int] = ..., nodeAccountId: _Optional[_Union[AccountID, _Mapping]] = ..., nodeCertHash: _Optional[bytes] = ..., serviceEndpoint: _Optional[_Iterable[_Union[ServiceEndpoint, _Mapping]]] = ..., description: _Optional[str] = ..., stake: _Optional[int] = ...) -> None: ...

class NodeAddressBook(_message.Message):
    __slots__ = ("nodeAddress",)
    NODEADDRESS_FIELD_NUMBER: _ClassVar[int]
    nodeAddress: _containers.RepeatedCompositeFieldContainer[NodeAddress]
    def __init__(self, nodeAddress: _Optional[_Iterable[_Union[NodeAddress, _Mapping]]] = ...) -> None: ...

class SemanticVersion(_message.Message):
    __slots__ = ("major", "minor", "patch", "pre", "build")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PRE_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    pre: str
    build: str
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ..., pre: _Optional[str] = ..., build: _Optional[str] = ...) -> None: ...

class Setting(_message.Message):
    __slots__ = ("name", "value", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    data: bytes
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class ServicesConfigurationList(_message.Message):
    __slots__ = ("nameValue",)
    NAMEVALUE_FIELD_NUMBER: _ClassVar[int]
    nameValue: _containers.RepeatedCompositeFieldContainer[Setting]
    def __init__(self, nameValue: _Optional[_Iterable[_Union[Setting, _Mapping]]] = ...) -> None: ...

class TokenRelationship(_message.Message):
    __slots__ = ("tokenId", "symbol", "balance", "kycStatus", "freezeStatus", "decimals", "automatic_association")
    TOKENID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    KYCSTATUS_FIELD_NUMBER: _ClassVar[int]
    FREEZESTATUS_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    tokenId: TokenID
    symbol: str
    balance: int
    kycStatus: TokenKycStatus
    freezeStatus: TokenFreezeStatus
    decimals: int
    automatic_association: bool
    def __init__(self, tokenId: _Optional[_Union[TokenID, _Mapping]] = ..., symbol: _Optional[str] = ..., balance: _Optional[int] = ..., kycStatus: _Optional[_Union[TokenKycStatus, str]] = ..., freezeStatus: _Optional[_Union[TokenFreezeStatus, str]] = ..., decimals: _Optional[int] = ..., automatic_association: bool = ...) -> None: ...

class TokenBalance(_message.Message):
    __slots__ = ("tokenId", "balance", "decimals")
    TOKENID_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    tokenId: TokenID
    balance: int
    decimals: int
    def __init__(self, tokenId: _Optional[_Union[TokenID, _Mapping]] = ..., balance: _Optional[int] = ..., decimals: _Optional[int] = ...) -> None: ...

class TokenBalances(_message.Message):
    __slots__ = ("tokenBalances",)
    TOKENBALANCES_FIELD_NUMBER: _ClassVar[int]
    tokenBalances: _containers.RepeatedCompositeFieldContainer[TokenBalance]
    def __init__(self, tokenBalances: _Optional[_Iterable[_Union[TokenBalance, _Mapping]]] = ...) -> None: ...

class TokenAssociation(_message.Message):
    __slots__ = ("token_id", "account_id")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: TokenID
    account_id: AccountID
    def __init__(self, token_id: _Optional[_Union[TokenID, _Mapping]] = ..., account_id: _Optional[_Union[AccountID, _Mapping]] = ...) -> None: ...

class StakingInfo(_message.Message):
    __slots__ = ("decline_reward", "stake_period_start", "pending_reward", "staked_to_me", "staked_account_id", "staked_node_id")
    DECLINE_REWARD_FIELD_NUMBER: _ClassVar[int]
    STAKE_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    PENDING_REWARD_FIELD_NUMBER: _ClassVar[int]
    STAKED_TO_ME_FIELD_NUMBER: _ClassVar[int]
    STAKED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STAKED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    decline_reward: bool
    stake_period_start: _timestamp_pb2.Timestamp
    pending_reward: int
    staked_to_me: int
    staked_account_id: AccountID
    staked_node_id: int
    def __init__(self, decline_reward: bool = ..., stake_period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pending_reward: _Optional[int] = ..., staked_to_me: _Optional[int] = ..., staked_account_id: _Optional[_Union[AccountID, _Mapping]] = ..., staked_node_id: _Optional[int] = ...) -> None: ...

class PendingAirdropId(_message.Message):
    __slots__ = ("sender_id", "receiver_id", "fungible_token_type", "non_fungible_token")
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    FUNGIBLE_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    NON_FUNGIBLE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sender_id: AccountID
    receiver_id: AccountID
    fungible_token_type: TokenID
    non_fungible_token: NftID
    def __init__(self, sender_id: _Optional[_Union[AccountID, _Mapping]] = ..., receiver_id: _Optional[_Union[AccountID, _Mapping]] = ..., fungible_token_type: _Optional[_Union[TokenID, _Mapping]] = ..., non_fungible_token: _Optional[_Union[NftID, _Mapping]] = ...) -> None: ...

class PendingAirdropValue(_message.Message):
    __slots__ = ("amount",)
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: int
    def __init__(self, amount: _Optional[int] = ...) -> None: ...
