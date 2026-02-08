from . import get_by_key_pb2 as _get_by_key_pb2
from . import get_by_solidity_id_pb2 as _get_by_solidity_id_pb2
from . import contract_call_local_pb2 as _contract_call_local_pb2
from . import contract_get_info_pb2 as _contract_get_info_pb2
from . import contract_get_bytecode_pb2 as _contract_get_bytecode_pb2
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
from . import token_get_info_pb2 as _token_get_info_pb2
from . import schedule_get_info_pb2 as _schedule_get_info_pb2
from . import token_get_account_nft_infos_pb2 as _token_get_account_nft_infos_pb2
from . import token_get_nft_info_pb2 as _token_get_nft_info_pb2
from . import token_get_nft_infos_pb2 as _token_get_nft_infos_pb2
from . import get_account_details_pb2 as _get_account_details_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Query(_message.Message):
    __slots__ = ("getByKey", "getBySolidityID", "contractCallLocal", "contractGetInfo", "contractGetBytecode", "ContractGetRecords", "cryptogetAccountBalance", "cryptoGetAccountRecords", "cryptoGetInfo", "cryptoGetLiveHash", "cryptoGetProxyStakers", "fileGetContents", "fileGetInfo", "transactionGetReceipt", "transactionGetRecord", "transactionGetFastRecord", "consensusGetTopicInfo", "networkGetVersionInfo", "tokenGetInfo", "scheduleGetInfo", "tokenGetAccountNftInfos", "tokenGetNftInfo", "tokenGetNftInfos", "networkGetExecutionTime", "accountDetails")
    GETBYKEY_FIELD_NUMBER: _ClassVar[int]
    GETBYSOLIDITYID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTCALLLOCAL_FIELD_NUMBER: _ClassVar[int]
    CONTRACTGETINFO_FIELD_NUMBER: _ClassVar[int]
    CONTRACTGETBYTECODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTGETRECORDS_FIELD_NUMBER: _ClassVar[int]
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
    getByKey: _get_by_key_pb2.GetByKeyQuery
    getBySolidityID: _get_by_solidity_id_pb2.GetBySolidityIDQuery
    contractCallLocal: _contract_call_local_pb2.ContractCallLocalQuery
    contractGetInfo: _contract_get_info_pb2.ContractGetInfoQuery
    contractGetBytecode: _contract_get_bytecode_pb2.ContractGetBytecodeQuery
    ContractGetRecords: _contract_get_records_pb2.ContractGetRecordsQuery
    cryptogetAccountBalance: _crypto_get_account_balance_pb2.CryptoGetAccountBalanceQuery
    cryptoGetAccountRecords: _crypto_get_account_records_pb2.CryptoGetAccountRecordsQuery
    cryptoGetInfo: _crypto_get_info_pb2.CryptoGetInfoQuery
    cryptoGetLiveHash: _crypto_get_live_hash_pb2.CryptoGetLiveHashQuery
    cryptoGetProxyStakers: _crypto_get_stakers_pb2.CryptoGetStakersQuery
    fileGetContents: _file_get_contents_pb2.FileGetContentsQuery
    fileGetInfo: _file_get_info_pb2.FileGetInfoQuery
    transactionGetReceipt: _transaction_get_receipt_pb2.TransactionGetReceiptQuery
    transactionGetRecord: _transaction_get_record_pb2.TransactionGetRecordQuery
    transactionGetFastRecord: _transaction_get_fast_record_pb2.TransactionGetFastRecordQuery
    consensusGetTopicInfo: _consensus_get_topic_info_pb2.ConsensusGetTopicInfoQuery
    networkGetVersionInfo: _network_get_version_info_pb2.NetworkGetVersionInfoQuery
    tokenGetInfo: _token_get_info_pb2.TokenGetInfoQuery
    scheduleGetInfo: _schedule_get_info_pb2.ScheduleGetInfoQuery
    tokenGetAccountNftInfos: _token_get_account_nft_infos_pb2.TokenGetAccountNftInfosQuery
    tokenGetNftInfo: _token_get_nft_info_pb2.TokenGetNftInfoQuery
    tokenGetNftInfos: _token_get_nft_infos_pb2.TokenGetNftInfosQuery
    networkGetExecutionTime: _network_get_execution_time_pb2.NetworkGetExecutionTimeQuery
    accountDetails: _get_account_details_pb2.GetAccountDetailsQuery
    def __init__(self, getByKey: _Optional[_Union[_get_by_key_pb2.GetByKeyQuery, _Mapping]] = ..., getBySolidityID: _Optional[_Union[_get_by_solidity_id_pb2.GetBySolidityIDQuery, _Mapping]] = ..., contractCallLocal: _Optional[_Union[_contract_call_local_pb2.ContractCallLocalQuery, _Mapping]] = ..., contractGetInfo: _Optional[_Union[_contract_get_info_pb2.ContractGetInfoQuery, _Mapping]] = ..., contractGetBytecode: _Optional[_Union[_contract_get_bytecode_pb2.ContractGetBytecodeQuery, _Mapping]] = ..., ContractGetRecords: _Optional[_Union[_contract_get_records_pb2.ContractGetRecordsQuery, _Mapping]] = ..., cryptogetAccountBalance: _Optional[_Union[_crypto_get_account_balance_pb2.CryptoGetAccountBalanceQuery, _Mapping]] = ..., cryptoGetAccountRecords: _Optional[_Union[_crypto_get_account_records_pb2.CryptoGetAccountRecordsQuery, _Mapping]] = ..., cryptoGetInfo: _Optional[_Union[_crypto_get_info_pb2.CryptoGetInfoQuery, _Mapping]] = ..., cryptoGetLiveHash: _Optional[_Union[_crypto_get_live_hash_pb2.CryptoGetLiveHashQuery, _Mapping]] = ..., cryptoGetProxyStakers: _Optional[_Union[_crypto_get_stakers_pb2.CryptoGetStakersQuery, _Mapping]] = ..., fileGetContents: _Optional[_Union[_file_get_contents_pb2.FileGetContentsQuery, _Mapping]] = ..., fileGetInfo: _Optional[_Union[_file_get_info_pb2.FileGetInfoQuery, _Mapping]] = ..., transactionGetReceipt: _Optional[_Union[_transaction_get_receipt_pb2.TransactionGetReceiptQuery, _Mapping]] = ..., transactionGetRecord: _Optional[_Union[_transaction_get_record_pb2.TransactionGetRecordQuery, _Mapping]] = ..., transactionGetFastRecord: _Optional[_Union[_transaction_get_fast_record_pb2.TransactionGetFastRecordQuery, _Mapping]] = ..., consensusGetTopicInfo: _Optional[_Union[_consensus_get_topic_info_pb2.ConsensusGetTopicInfoQuery, _Mapping]] = ..., networkGetVersionInfo: _Optional[_Union[_network_get_version_info_pb2.NetworkGetVersionInfoQuery, _Mapping]] = ..., tokenGetInfo: _Optional[_Union[_token_get_info_pb2.TokenGetInfoQuery, _Mapping]] = ..., scheduleGetInfo: _Optional[_Union[_schedule_get_info_pb2.ScheduleGetInfoQuery, _Mapping]] = ..., tokenGetAccountNftInfos: _Optional[_Union[_token_get_account_nft_infos_pb2.TokenGetAccountNftInfosQuery, _Mapping]] = ..., tokenGetNftInfo: _Optional[_Union[_token_get_nft_info_pb2.TokenGetNftInfoQuery, _Mapping]] = ..., tokenGetNftInfos: _Optional[_Union[_token_get_nft_infos_pb2.TokenGetNftInfosQuery, _Mapping]] = ..., networkGetExecutionTime: _Optional[_Union[_network_get_execution_time_pb2.NetworkGetExecutionTimeQuery, _Mapping]] = ..., accountDetails: _Optional[_Union[_get_account_details_pb2.GetAccountDetailsQuery, _Mapping]] = ...) -> None: ...
