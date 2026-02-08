from google.protobuf import wrappers_pb2 as _wrappers_pb2
from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeUpdateTransactionBody(_message.Message):
    __slots__ = ("node_id", "account_id", "description", "gossip_endpoint", "service_endpoint", "gossip_ca_certificate", "grpc_certificate_hash", "admin_key", "decline_reward", "grpc_proxy_endpoint")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GOSSIP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    GOSSIP_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    GRPC_CERTIFICATE_HASH_FIELD_NUMBER: _ClassVar[int]
    ADMIN_KEY_FIELD_NUMBER: _ClassVar[int]
    DECLINE_REWARD_FIELD_NUMBER: _ClassVar[int]
    GRPC_PROXY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    account_id: _basic_types_pb2.AccountID
    description: _wrappers_pb2.StringValue
    gossip_endpoint: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.ServiceEndpoint]
    service_endpoint: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.ServiceEndpoint]
    gossip_ca_certificate: _wrappers_pb2.BytesValue
    grpc_certificate_hash: _wrappers_pb2.BytesValue
    admin_key: _basic_types_pb2.Key
    decline_reward: _wrappers_pb2.BoolValue
    grpc_proxy_endpoint: _basic_types_pb2.ServiceEndpoint
    def __init__(self, node_id: _Optional[int] = ..., account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., gossip_endpoint: _Optional[_Iterable[_Union[_basic_types_pb2.ServiceEndpoint, _Mapping]]] = ..., service_endpoint: _Optional[_Iterable[_Union[_basic_types_pb2.ServiceEndpoint, _Mapping]]] = ..., gossip_ca_certificate: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., grpc_certificate_hash: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., admin_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., decline_reward: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., grpc_proxy_endpoint: _Optional[_Union[_basic_types_pb2.ServiceEndpoint, _Mapping]] = ...) -> None: ...
