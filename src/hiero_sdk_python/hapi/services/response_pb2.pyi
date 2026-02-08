from . import get_by_key_pb2 as _get_by_key_pb2
from . import get_by_solidity_id_pb2 as _get_by_solidity_id_pb2
from . import contract_call_local_pb2 as _contract_call_local_pb2
from . import contract_get_bytecode_pb2 as _contract_get_bytecode_pb2
from . import contract_get_info_pb2 as _contract_get_info_pb2
from . import contract_get_records_pb2 as _contract_get_records_pb2
from . import crypto_get_account_balance_pb2 as _crypto_get_account_balance_pb2
from . import crypto_get_account_records_pb2 as _crypto_get_account_records_pb2
from . import crypto_get_info_pb2 as _crypto_get_info_pb2
from . import crypto_get_live_hash_pb2 as _crypto_get_live_hash_pb2
from . import crypto_get_stakers_pb2 as _crypto_get_stakers_pb2
from . import file_get_contents_pb2 as _file_get_contents_pb2
from . import file_get_info_pb2 as _file_get_info_pb2
from . import transaction_get_receipt_pb2 as _transaction_get_receipt_pb2
from . import transaction_get_record_pb2 as _transaction_get_record_pb2
from . import transaction_get_fast_record_pb2 as _transaction_get_fast_record_pb2
from . import consensus_get_topic_info_pb2 as _consensus_get_topic_info_pb2
from . import network_get_version_info_pb2 as _network_get_version_info_pb2
from . import network_get_execution_time_pb2 as _network_get_execution_time_pb2
from . import token_get_account_nft_infos_pb2 as _token_get_account_nft_infos_pb2
from . import token_get_info_pb2 as _token_get_info_pb2
from . import token_get_nft_info_pb2 as _token_get_nft_info_pb2
from . import token_get_nft_infos_pb2 as _token_get_nft_infos_pb2
from . import schedule_get_info_pb2 as _schedule_get_info_pb2
from . import get_account_details_pb2 as _get_account_details_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("getByKey", "getBySolidityID", "contractCallLocal", "contractGetBytecodeResponse", "contractGetInfo", "contractGetRecordsResponse", "cryptogetAccountBalance", "cryptoGetAccountRecords", "cryptoGetInfo", "cryptoGetLiveHash", "cryptoGetProxyStakers", "fileGetContents", "fileGetInfo", "transactionGetReceipt", "transactionGetRecord", "transactionGetFastRecord", "consensusGetTopicInfo", "networkGetVersionInfo", "tokenGetInfo", "scheduleGetInfo", "tokenGetAccountNftInfos", "tokenGetNftInfo", "tokenGetNftInfos", "networkGetExecutionTime", "accountDetails")
    GETBYKEY_FIELD_NUMBER: _ClassVar[int]
    GETBYSOLIDITYID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTCALLLOCAL_FIELD_NUMBER: _ClassVar[int]
    CONTRACTGETBYTECODERESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTGETINFO_FIELD_NUMBER: _ClassVar[int]
    CONTRACTGETRECORDSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOGETACCOUNTBALANCE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOGETACCOUNTRECORDS_FIELD_NUMBER: _ClassVar[int]
    CRYPTOGETINFO_FIELD_NUMBER: _ClassVar[int]
    CRYPTOGETLIVEHASH_FIELD_NUMBER: _ClassVar[int]
    CRYPTOGETPROXYSTAKERS_FIELD_NUMBER: _ClassVar[int]
    FILEGETCONTENTS_FIELD_NUMBER: _ClassVar[int]
    FILEGETINFO_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONGETRECEIPT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONGETRECORD_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONGETFASTRECORD_FIELD_NUMBER: _ClassVar[int]
    CONSENSUSGETTOPICINFO_FIELD_NUMBER: _ClassVar[int]
    NETWORKGETVERSIONINFO_FIELD_NUMBER: _ClassVar[int]
    TOKENGETINFO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEGETINFO_FIELD_NUMBER: _ClassVar[int]
    TOKENGETACCOUNTNFTINFOS_FIELD_NUMBER: _ClassVar[int]
    TOKENGETNFTINFO_FIELD_NUMBER: _ClassVar[int]
    TOKENGETNFTINFOS_FIELD_NUMBER: _ClassVar[int]
    NETWORKGETEXECUTIONTIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTDETAILS_FIELD_NUMBER: _ClassVar[int]
    getByKey: _get_by_key_pb2.GetByKeyResponse
    getBySolidityID: _get_by_solidity_id_pb2.GetBySolidityIDResponse
    contractCallLocal: _contract_call_local_pb2.ContractCallLocalResponse
    contractGetBytecodeResponse: _contract_get_bytecode_pb2.ContractGetBytecodeResponse
    contractGetInfo: _contract_get_info_pb2.ContractGetInfoResponse
    contractGetRecordsResponse: _contract_get_records_pb2.ContractGetRecordsResponse
    cryptogetAccountBalance: _crypto_get_account_balance_pb2.CryptoGetAccountBalanceResponse
    cryptoGetAccountRecords: _crypto_get_account_records_pb2.CryptoGetAccountRecordsResponse
    cryptoGetInfo: _crypto_get_info_pb2.CryptoGetInfoResponse
    cryptoGetLiveHash: _crypto_get_live_hash_pb2.CryptoGetLiveHashResponse
    cryptoGetProxyStakers: _crypto_get_stakers_pb2.CryptoGetStakersResponse
    fileGetContents: _file_get_contents_pb2.FileGetContentsResponse
    fileGetInfo: _file_get_info_pb2.FileGetInfoResponse
    transactionGetReceipt: _transaction_get_receipt_pb2.TransactionGetReceiptResponse
    transactionGetRecord: _transaction_get_record_pb2.TransactionGetRecordResponse
    transactionGetFastRecord: _transaction_get_fast_record_pb2.TransactionGetFastRecordResponse
    consensusGetTopicInfo: _consensus_get_topic_info_pb2.ConsensusGetTopicInfoResponse
    networkGetVersionInfo: _network_get_version_info_pb2.NetworkGetVersionInfoResponse
    tokenGetInfo: _token_get_info_pb2.TokenGetInfoResponse
    scheduleGetInfo: _schedule_get_info_pb2.ScheduleGetInfoResponse
    tokenGetAccountNftInfos: _token_get_account_nft_infos_pb2.TokenGetAccountNftInfosResponse
    tokenGetNftInfo: _token_get_nft_info_pb2.TokenGetNftInfoResponse
    tokenGetNftInfos: _token_get_nft_infos_pb2.TokenGetNftInfosResponse
    networkGetExecutionTime: _network_get_execution_time_pb2.NetworkGetExecutionTimeResponse
    accountDetails: _get_account_details_pb2.GetAccountDetailsResponse
    def __init__(self, getByKey: _Optional[_Union[_get_by_key_pb2.GetByKeyResponse, _Mapping]] = ..., getBySolidityID: _Optional[_Union[_get_by_solidity_id_pb2.GetBySolidityIDResponse, _Mapping]] = ..., contractCallLocal: _Optional[_Union[_contract_call_local_pb2.ContractCallLocalResponse, _Mapping]] = ..., contractGetBytecodeResponse: _Optional[_Union[_contract_get_bytecode_pb2.ContractGetBytecodeResponse, _Mapping]] = ..., contractGetInfo: _Optional[_Union[_contract_get_info_pb2.ContractGetInfoResponse, _Mapping]] = ..., contractGetRecordsResponse: _Optional[_Union[_contract_get_records_pb2.ContractGetRecordsResponse, _Mapping]] = ..., cryptogetAccountBalance: _Optional[_Union[_crypto_get_account_balance_pb2.CryptoGetAccountBalanceResponse, _Mapping]] = ..., cryptoGetAccountRecords: _Optional[_Union[_crypto_get_account_records_pb2.CryptoGetAccountRecordsResponse, _Mapping]] = ..., cryptoGetInfo: _Optional[_Union[_crypto_get_info_pb2.CryptoGetInfoResponse, _Mapping]] = ..., cryptoGetLiveHash: _Optional[_Union[_crypto_get_live_hash_pb2.CryptoGetLiveHashResponse, _Mapping]] = ..., cryptoGetProxyStakers: _Optional[_Union[_crypto_get_stakers_pb2.CryptoGetStakersResponse, _Mapping]] = ..., fileGetContents: _Optional[_Union[_file_get_contents_pb2.FileGetContentsResponse, _Mapping]] = ..., fileGetInfo: _Optional[_Union[_file_get_info_pb2.FileGetInfoResponse, _Mapping]] = ..., transactionGetReceipt: _Optional[_Union[_transaction_get_receipt_pb2.TransactionGetReceiptResponse, _Mapping]] = ..., transactionGetRecord: _Optional[_Union[_transaction_get_record_pb2.TransactionGetRecordResponse, _Mapping]] = ..., transactionGetFastRecord: _Optional[_Union[_transaction_get_fast_record_pb2.TransactionGetFastRecordResponse, _Mapping]] = ..., consensusGetTopicInfo: _Optional[_Union[_consensus_get_topic_info_pb2.ConsensusGetTopicInfoResponse, _Mapping]] = ..., networkGetVersionInfo: _Optional[_Union[_network_get_version_info_pb2.NetworkGetVersionInfoResponse, _Mapping]] = ..., tokenGetInfo: _Optional[_Union[_token_get_info_pb2.TokenGetInfoResponse, _Mapping]] = ..., scheduleGetInfo: _Optional[_Union[_schedule_get_info_pb2.ScheduleGetInfoResponse, _Mapping]] = ..., tokenGetAccountNftInfos: _Optional[_Union[_token_get_account_nft_infos_pb2.TokenGetAccountNftInfosResponse, _Mapping]] = ..., tokenGetNftInfo: _Optional[_Union[_token_get_nft_info_pb2.TokenGetNftInfoResponse, _Mapping]] = ..., tokenGetNftInfos: _Optional[_Union[_token_get_nft_infos_pb2.TokenGetNftInfosResponse, _Mapping]] = ..., networkGetExecutionTime: _Optional[_Union[_network_get_execution_time_pb2.NetworkGetExecutionTimeResponse, _Mapping]] = ..., accountDetails: _Optional[_Union[_get_account_details_pb2.GetAccountDetailsResponse, _Mapping]] = ...) -> None: ...
