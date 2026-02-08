from . import system_delete_pb2 as _system_delete_pb2
from . import system_undelete_pb2 as _system_undelete_pb2
from . import freeze_pb2 as _freeze_pb2
from . import contract_call_pb2 as _contract_call_pb2
from . import contract_create_pb2 as _contract_create_pb2
from . import contract_update_pb2 as _contract_update_pb2
from . import crypto_create_pb2 as _crypto_create_pb2
from . import crypto_delete_pb2 as _crypto_delete_pb2
from . import crypto_transfer_pb2 as _crypto_transfer_pb2
from . import crypto_update_pb2 as _crypto_update_pb2
from . import crypto_approve_allowance_pb2 as _crypto_approve_allowance_pb2
from . import crypto_delete_allowance_pb2 as _crypto_delete_allowance_pb2
from . import file_append_pb2 as _file_append_pb2
from . import file_create_pb2 as _file_create_pb2
from . import file_delete_pb2 as _file_delete_pb2
from . import file_update_pb2 as _file_update_pb2
from . import contract_delete_pb2 as _contract_delete_pb2
from . import consensus_create_topic_pb2 as _consensus_create_topic_pb2
from . import consensus_update_topic_pb2 as _consensus_update_topic_pb2
from . import consensus_delete_topic_pb2 as _consensus_delete_topic_pb2
from . import consensus_submit_message_pb2 as _consensus_submit_message_pb2
from . import token_create_pb2 as _token_create_pb2
from . import token_freeze_account_pb2 as _token_freeze_account_pb2
from . import token_unfreeze_account_pb2 as _token_unfreeze_account_pb2
from . import token_grant_kyc_pb2 as _token_grant_kyc_pb2
from . import token_revoke_kyc_pb2 as _token_revoke_kyc_pb2
from . import token_delete_pb2 as _token_delete_pb2
from . import token_update_pb2 as _token_update_pb2
from . import token_mint_pb2 as _token_mint_pb2
from . import token_burn_pb2 as _token_burn_pb2
from . import token_wipe_account_pb2 as _token_wipe_account_pb2
from . import token_associate_pb2 as _token_associate_pb2
from . import token_dissociate_pb2 as _token_dissociate_pb2
from . import token_fee_schedule_update_pb2 as _token_fee_schedule_update_pb2
from . import token_pause_pb2 as _token_pause_pb2
from . import token_unpause_pb2 as _token_unpause_pb2
from . import token_update_nfts_pb2 as _token_update_nfts_pb2
from . import token_reject_pb2 as _token_reject_pb2
from . import token_cancel_airdrop_pb2 as _token_cancel_airdrop_pb2
from . import token_claim_airdrop_pb2 as _token_claim_airdrop_pb2
from . import token_airdrop_pb2 as _token_airdrop_pb2
from . import schedule_delete_pb2 as _schedule_delete_pb2
from . import util_prng_pb2 as _util_prng_pb2
from . import custom_fees_pb2 as _custom_fees_pb2
from . import node_create_pb2 as _node_create_pb2
from . import node_update_pb2 as _node_update_pb2
from . import node_delete_pb2 as _node_delete_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SchedulableTransactionBody(_message.Message):
    __slots__ = ("transactionFee", "memo", "contractCall", "contractCreateInstance", "contractUpdateInstance", "contractDeleteInstance", "cryptoCreateAccount", "cryptoDelete", "cryptoTransfer", "cryptoUpdateAccount", "fileAppend", "fileCreate", "fileDelete", "fileUpdate", "systemDelete", "systemUndelete", "freeze", "consensusCreateTopic", "consensusUpdateTopic", "consensusDeleteTopic", "consensusSubmitMessage", "tokenCreation", "tokenFreeze", "tokenUnfreeze", "tokenGrantKyc", "tokenRevokeKyc", "tokenDeletion", "tokenUpdate", "tokenMint", "tokenBurn", "tokenWipe", "tokenAssociate", "tokenDissociate", "scheduleDelete", "token_pause", "token_unpause", "cryptoApproveAllowance", "cryptoDeleteAllowance", "token_fee_schedule_update", "util_prng", "token_update_nfts", "nodeCreate", "nodeUpdate", "nodeDelete", "tokenReject", "tokenCancelAirdrop", "tokenClaimAirdrop", "tokenAirdrop", "max_custom_fees")
    TRANSACTIONFEE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    CONTRACTCALL_FIELD_NUMBER: _ClassVar[int]
    CONTRACTCREATEINSTANCE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTUPDATEINSTANCE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTDELETEINSTANCE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOCREATEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CRYPTODELETE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOTRANSFER_FIELD_NUMBER: _ClassVar[int]
    CRYPTOUPDATEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    FILEAPPEND_FIELD_NUMBER: _ClassVar[int]
    FILECREATE_FIELD_NUMBER: _ClassVar[int]
    FILEDELETE_FIELD_NUMBER: _ClassVar[int]
    FILEUPDATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEMDELETE_FIELD_NUMBER: _ClassVar[int]
    SYSTEMUNDELETE_FIELD_NUMBER: _ClassVar[int]
    FREEZE_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSCREATETOPIC_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSUPDATETOPIC_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSDELETETOPIC_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSSUBMITMESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKENCREATION_FIELD_NUMBER: _ClassVar[int]
    TOKENFREEZE_FIELD_NUMBER: _ClassVar[int]
    TOKENUNFREEZE_FIELD_NUMBER: _ClassVar[int]
    TOKENGRANTKYC_FIELD_NUMBER: _ClassVar[int]
    TOKENREVOKEKYC_FIELD_NUMBER: _ClassVar[int]
    TOKENDELETION_FIELD_NUMBER: _ClassVar[int]
    TOKENUPDATE_FIELD_NUMBER: _ClassVar[int]
    TOKENMINT_FIELD_NUMBER: _ClassVar[int]
    TOKENBURN_FIELD_NUMBER: _ClassVar[int]
    TOKENWIPE_FIELD_NUMBER: _ClassVar[int]
    TOKENASSOCIATE_FIELD_NUMBER: _ClassVar[int]
    TOKENDISSOCIATE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDELETE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_PAUSE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_UNPAUSE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOAPPROVEALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    CRYPTODELETEALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FEE_SCHEDULE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UTIL_PRNG_FIELD_NUMBER: _ClassVar[int]
    TOKEN_UPDATE_NFTS_FIELD_NUMBER: _ClassVar[int]
    NODECREATE_FIELD_NUMBER: _ClassVar[int]
    NODEUPDATE_FIELD_NUMBER: _ClassVar[int]
    NODEDELETE_FIELD_NUMBER: _ClassVar[int]
    TOKENREJECT_FIELD_NUMBER: _ClassVar[int]
    TOKENCANCELAIRDROP_FIELD_NUMBER: _ClassVar[int]
    TOKENCLAIMAIRDROP_FIELD_NUMBER: _ClassVar[int]
    TOKENAIRDROP_FIELD_NUMBER: _ClassVar[int]
    MAX_CUSTOM_FEES_FIELD_NUMBER: _ClassVar[int]
    transactionFee: int
    memo: str
    contractCall: _contract_call_pb2.ContractCallTransactionBody
    contractCreateInstance: _contract_create_pb2.ContractCreateTransactionBody
    contractUpdateInstance: _contract_update_pb2.ContractUpdateTransactionBody
    contractDeleteInstance: _contract_delete_pb2.ContractDeleteTransactionBody
    cryptoCreateAccount: _crypto_create_pb2.CryptoCreateTransactionBody
    cryptoDelete: _crypto_delete_pb2.CryptoDeleteTransactionBody
    cryptoTransfer: _crypto_transfer_pb2.CryptoTransferTransactionBody
    cryptoUpdateAccount: _crypto_update_pb2.CryptoUpdateTransactionBody
    fileAppend: _file_append_pb2.FileAppendTransactionBody
    fileCreate: _file_create_pb2.FileCreateTransactionBody
    fileDelete: _file_delete_pb2.FileDeleteTransactionBody
    fileUpdate: _file_update_pb2.FileUpdateTransactionBody
    systemDelete: _system_delete_pb2.SystemDeleteTransactionBody
    systemUndelete: _system_undelete_pb2.SystemUndeleteTransactionBody
    freeze: _freeze_pb2.FreezeTransactionBody
    consensusCreateTopic: _consensus_create_topic_pb2.ConsensusCreateTopicTransactionBody
    consensusUpdateTopic: _consensus_update_topic_pb2.ConsensusUpdateTopicTransactionBody
    consensusDeleteTopic: _consensus_delete_topic_pb2.ConsensusDeleteTopicTransactionBody
    consensusSubmitMessage: _consensus_submit_message_pb2.ConsensusSubmitMessageTransactionBody
    tokenCreation: _token_create_pb2.TokenCreateTransactionBody
    tokenFreeze: _token_freeze_account_pb2.TokenFreezeAccountTransactionBody
    tokenUnfreeze: _token_unfreeze_account_pb2.TokenUnfreezeAccountTransactionBody
    tokenGrantKyc: _token_grant_kyc_pb2.TokenGrantKycTransactionBody
    tokenRevokeKyc: _token_revoke_kyc_pb2.TokenRevokeKycTransactionBody
    tokenDeletion: _token_delete_pb2.TokenDeleteTransactionBody
    tokenUpdate: _token_update_pb2.TokenUpdateTransactionBody
    tokenMint: _token_mint_pb2.TokenMintTransactionBody
    tokenBurn: _token_burn_pb2.TokenBurnTransactionBody
    tokenWipe: _token_wipe_account_pb2.TokenWipeAccountTransactionBody
    tokenAssociate: _token_associate_pb2.TokenAssociateTransactionBody
    tokenDissociate: _token_dissociate_pb2.TokenDissociateTransactionBody
    scheduleDelete: _schedule_delete_pb2.ScheduleDeleteTransactionBody
    token_pause: _token_pause_pb2.TokenPauseTransactionBody
    token_unpause: _token_unpause_pb2.TokenUnpauseTransactionBody
    cryptoApproveAllowance: _crypto_approve_allowance_pb2.CryptoApproveAllowanceTransactionBody
    cryptoDeleteAllowance: _crypto_delete_allowance_pb2.CryptoDeleteAllowanceTransactionBody
    token_fee_schedule_update: _token_fee_schedule_update_pb2.TokenFeeScheduleUpdateTransactionBody
    util_prng: _util_prng_pb2.UtilPrngTransactionBody
    token_update_nfts: _token_update_nfts_pb2.TokenUpdateNftsTransactionBody
    nodeCreate: _node_create_pb2.NodeCreateTransactionBody
    nodeUpdate: _node_update_pb2.NodeUpdateTransactionBody
    nodeDelete: _node_delete_pb2.NodeDeleteTransactionBody
    tokenReject: _token_reject_pb2.TokenRejectTransactionBody
    tokenCancelAirdrop: _token_cancel_airdrop_pb2.TokenCancelAirdropTransactionBody
    tokenClaimAirdrop: _token_claim_airdrop_pb2.TokenClaimAirdropTransactionBody
    tokenAirdrop: _token_airdrop_pb2.TokenAirdropTransactionBody
    max_custom_fees: _containers.RepeatedCompositeFieldContainer[_custom_fees_pb2.CustomFeeLimit]
    def __init__(self, transactionFee: _Optional[int] = ..., memo: _Optional[str] = ..., contractCall: _Optional[_Union[_contract_call_pb2.ContractCallTransactionBody, _Mapping]] = ..., contractCreateInstance: _Optional[_Union[_contract_create_pb2.ContractCreateTransactionBody, _Mapping]] = ..., contractUpdateInstance: _Optional[_Union[_contract_update_pb2.ContractUpdateTransactionBody, _Mapping]] = ..., contractDeleteInstance: _Optional[_Union[_contract_delete_pb2.ContractDeleteTransactionBody, _Mapping]] = ..., cryptoCreateAccount: _Optional[_Union[_crypto_create_pb2.CryptoCreateTransactionBody, _Mapping]] = ..., cryptoDelete: _Optional[_Union[_crypto_delete_pb2.CryptoDeleteTransactionBody, _Mapping]] = ..., cryptoTransfer: _Optional[_Union[_crypto_transfer_pb2.CryptoTransferTransactionBody, _Mapping]] = ..., cryptoUpdateAccount: _Optional[_Union[_crypto_update_pb2.CryptoUpdateTransactionBody, _Mapping]] = ..., fileAppend: _Optional[_Union[_file_append_pb2.FileAppendTransactionBody, _Mapping]] = ..., fileCreate: _Optional[_Union[_file_create_pb2.FileCreateTransactionBody, _Mapping]] = ..., fileDelete: _Optional[_Union[_file_delete_pb2.FileDeleteTransactionBody, _Mapping]] = ..., fileUpdate: _Optional[_Union[_file_update_pb2.FileUpdateTransactionBody, _Mapping]] = ..., systemDelete: _Optional[_Union[_system_delete_pb2.SystemDeleteTransactionBody, _Mapping]] = ..., systemUndelete: _Optional[_Union[_system_undelete_pb2.SystemUndeleteTransactionBody, _Mapping]] = ..., freeze: _Optional[_Union[_freeze_pb2.FreezeTransactionBody, _Mapping]] = ..., consensusCreateTopic: _Optional[_Union[_consensus_create_topic_pb2.ConsensusCreateTopicTransactionBody, _Mapping]] = ..., consensusUpdateTopic: _Optional[_Union[_consensus_update_topic_pb2.ConsensusUpdateTopicTransactionBody, _Mapping]] = ..., consensusDeleteTopic: _Optional[_Union[_consensus_delete_topic_pb2.ConsensusDeleteTopicTransactionBody, _Mapping]] = ..., consensusSubmitMessage: _Optional[_Union[_consensus_submit_message_pb2.ConsensusSubmitMessageTransactionBody, _Mapping]] = ..., tokenCreation: _Optional[_Union[_token_create_pb2.TokenCreateTransactionBody, _Mapping]] = ..., tokenFreeze: _Optional[_Union[_token_freeze_account_pb2.TokenFreezeAccountTransactionBody, _Mapping]] = ..., tokenUnfreeze: _Optional[_Union[_token_unfreeze_account_pb2.TokenUnfreezeAccountTransactionBody, _Mapping]] = ..., tokenGrantKyc: _Optional[_Union[_token_grant_kyc_pb2.TokenGrantKycTransactionBody, _Mapping]] = ..., tokenRevokeKyc: _Optional[_Union[_token_revoke_kyc_pb2.TokenRevokeKycTransactionBody, _Mapping]] = ..., tokenDeletion: _Optional[_Union[_token_delete_pb2.TokenDeleteTransactionBody, _Mapping]] = ..., tokenUpdate: _Optional[_Union[_token_update_pb2.TokenUpdateTransactionBody, _Mapping]] = ..., tokenMint: _Optional[_Union[_token_mint_pb2.TokenMintTransactionBody, _Mapping]] = ..., tokenBurn: _Optional[_Union[_token_burn_pb2.TokenBurnTransactionBody, _Mapping]] = ..., tokenWipe: _Optional[_Union[_token_wipe_account_pb2.TokenWipeAccountTransactionBody, _Mapping]] = ..., tokenAssociate: _Optional[_Union[_token_associate_pb2.TokenAssociateTransactionBody, _Mapping]] = ..., tokenDissociate: _Optional[_Union[_token_dissociate_pb2.TokenDissociateTransactionBody, _Mapping]] = ..., scheduleDelete: _Optional[_Union[_schedule_delete_pb2.ScheduleDeleteTransactionBody, _Mapping]] = ..., token_pause: _Optional[_Union[_token_pause_pb2.TokenPauseTransactionBody, _Mapping]] = ..., token_unpause: _Optional[_Union[_token_unpause_pb2.TokenUnpauseTransactionBody, _Mapping]] = ..., cryptoApproveAllowance: _Optional[_Union[_crypto_approve_allowance_pb2.CryptoApproveAllowanceTransactionBody, _Mapping]] = ..., cryptoDeleteAllowance: _Optional[_Union[_crypto_delete_allowance_pb2.CryptoDeleteAllowanceTransactionBody, _Mapping]] = ..., token_fee_schedule_update: _Optional[_Union[_token_fee_schedule_update_pb2.TokenFeeScheduleUpdateTransactionBody, _Mapping]] = ..., util_prng: _Optional[_Union[_util_prng_pb2.UtilPrngTransactionBody, _Mapping]] = ..., token_update_nfts: _Optional[_Union[_token_update_nfts_pb2.TokenUpdateNftsTransactionBody, _Mapping]] = ..., nodeCreate: _Optional[_Union[_node_create_pb2.NodeCreateTransactionBody, _Mapping]] = ..., nodeUpdate: _Optional[_Union[_node_update_pb2.NodeUpdateTransactionBody, _Mapping]] = ..., nodeDelete: _Optional[_Union[_node_delete_pb2.NodeDeleteTransactionBody, _Mapping]] = ..., tokenReject: _Optional[_Union[_token_reject_pb2.TokenRejectTransactionBody, _Mapping]] = ..., tokenCancelAirdrop: _Optional[_Union[_token_cancel_airdrop_pb2.TokenCancelAirdropTransactionBody, _Mapping]] = ..., tokenClaimAirdrop: _Optional[_Union[_token_claim_airdrop_pb2.TokenClaimAirdropTransactionBody, _Mapping]] = ..., tokenAirdrop: _Optional[_Union[_token_airdrop_pb2.TokenAirdropTransactionBody, _Mapping]] = ..., max_custom_fees: _Optional[_Iterable[_Union[_custom_fees_pb2.CustomFeeLimit, _Mapping]]] = ...) -> None: ...
