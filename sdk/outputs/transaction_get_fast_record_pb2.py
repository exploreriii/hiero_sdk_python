# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: transaction_get_fast_record.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'transaction_get_fast_record.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import transaction_record_pb2 as transaction__record__pb2
from . import basic_types_pb2 as basic__types__pb2
from . import query_header_pb2 as query__header__pb2
from . import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!transaction_get_fast_record.proto\x12\x05proto\x1a\x18transaction_record.proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"p\n\x1dTransactionGetFastRecordQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12+\n\rtransactionID\x18\x02 \x01(\x0b\x32\x14.proto.TransactionID\"~\n TransactionGetFastRecordResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x33\n\x11transactionRecord\x18\x02 \x01(\x0b\x32\x18.proto.TransactionRecordB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transaction_get_fast_record_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_TRANSACTIONGETFASTRECORDQUERY']._serialized_start=132
  _globals['_TRANSACTIONGETFASTRECORDQUERY']._serialized_end=244
  _globals['_TRANSACTIONGETFASTRECORDRESPONSE']._serialized_start=246
  _globals['_TRANSACTIONGETFASTRECORDRESPONSE']._serialized_end=372
# @@protoc_insertion_point(module_scope)
