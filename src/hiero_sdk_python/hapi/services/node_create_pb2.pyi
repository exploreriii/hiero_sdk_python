from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeCreateTransactionBody(_message.Message):
    __slots__ = ("account_id", "description", "gossip_endpoint", "service_endpoint", "gossip_ca_certificate", "grpc_certificate_hash", "admin_key", "decline_reward", "grpc_proxy_endpoint")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GOSSIP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    GOSSIP_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    GRPC_CERTIFICATE_HASH_FIELD_NUMBER: _ClassVar[int]
    ADMIN_KEY_FIELD_NUMBER: _ClassVar[int]
    DECLINE_REWARD_FIELD_NUMBER: _ClassVar[int]
    GRPC_PROXY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    account_id: _basic_types_pb2.AccountID
    description: str
    gossip_endpoint: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.ServiceEndpoint]
    service_endpoint: _containers.RepeatedCompositeFieldContainer[_basic_types_pb2.ServiceEndpoint]
    gossip_ca_certificate: bytes
    grpc_certificate_hash: bytes
    admin_key: _basic_types_pb2.Key
    decline_reward: bool
    grpc_proxy_endpoint: _basic_types_pb2.ServiceEndpoint
    def __init__(self, account_id: _Optional[_Union[_basic_types_pb2.AccountID, _Mapping]] = ..., description: _Optional[str] = ..., gossip_endpoint: _Optional[_Iterable[_Union[_basic_types_pb2.ServiceEndpoint, _Mapping]]] = ..., service_endpoint: _Optional[_Iterable[_Union[_basic_types_pb2.ServiceEndpoint, _Mapping]]] = ..., gossip_ca_certificate: _Optional[bytes] = ..., grpc_certificate_hash: _Optional[bytes] = ..., admin_key: _Optional[_Union[_basic_types_pb2.Key, _Mapping]] = ..., decline_reward: bool = ..., grpc_proxy_endpoint: _Optional[_Union[_basic_types_pb2.ServiceEndpoint, _Mapping]] = ...) -> None: ...
