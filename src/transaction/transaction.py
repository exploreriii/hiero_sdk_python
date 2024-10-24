from src.proto import (
    transaction_pb2, transaction_body_pb2, basic_types_pb2,
    transaction_contents_pb2, duration_pb2, timestamp_pb2
)
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import time

class Transaction:
    """
    Base class for all Hedera transactions.

    This class provides common functionality for building, signing, and executing transactions
    on the Hedera network. Subclasses should implement the abstract methods to define
    transaction-specific behavior.
    """

    def __init__(self):
        """
        Initializes a new Transaction instance with default values.
        """
        self.transaction_id = None
        self.node_account_id = None
        self.transaction_fee = None
        self.transaction_valid_duration = 120 
        self.generate_record = False
        self.memo = ""
        self.transaction_body_bytes = None
        self.signature_map = basic_types_pb2.SignatureMap()

        self._default_transaction_fee = 2_000_000  

        self.operator_account_id = None  

    def sign(self, private_key):
        """
        Signs the transaction using the provided private key.

        Args:
            private_key (PrivateKey): The private key to sign the transaction with.

        Returns:
            Transaction: The current transaction instance for method chaining.

        Raises:
            Exception: If the transaction body has not been built.
        """
        if self.transaction_body_bytes is None:
            self.transaction_body_bytes = self.build_transaction_body().SerializeToString()

        signature = private_key.sign(self.transaction_body_bytes)

        public_key_bytes = private_key.public_key().public_bytes(
            encoding=Encoding.Raw,
            format=PublicFormat.Raw
        )

        sig_pair = basic_types_pb2.SignaturePair(
            pubKeyPrefix=public_key_bytes,
            ed25519=signature
        )

        self.signature_map.sigPair.append(sig_pair)

        return self

    def to_proto(self):
        """
        Converts the transaction to its protobuf representation.

        Returns:
            Transaction: The protobuf Transaction message.

        Raises:
            Exception: If the transaction body has not been built.
        """
        if self.transaction_body_bytes is None:
            raise Exception("Transaction must be signed before calling to_proto()")

        signed_transaction = transaction_contents_pb2.SignedTransaction(
            bodyBytes=self.transaction_body_bytes,
            sigMap=self.signature_map
        )

        return transaction_pb2.Transaction(
            signedTransactionBytes=signed_transaction.SerializeToString()
        )

    def freeze_with(self, client):
        """
        Freezes the transaction by building the transaction body and setting necessary IDs.

        Args:
            client (Client): The client instance to use for setting defaults.

        Returns:
            Transaction: The current transaction instance for method chaining.

        Raises:
            Exception: If required IDs are not set.
        """
        if self.transaction_body_bytes is not None:
            # transaction is already frozen
            return self

        if self.transaction_id is None:
            self.transaction_id = client.generate_transaction_id()

        if self.node_account_id is None:
            self.node_account_id = client.network.node_account_id

        self.transaction_body_bytes = self.build_transaction_body().SerializeToString()

        return self

    def execute(self, client):
        """
        Executes the transaction on the Hedera network using the provided client.

        Args:
            client (Client): The client instance to use for execution.

        Returns:
            TransactionReceipt or appropriate response based on transaction type.

        Raises:
            Exception: If execution fails.
        """
        if self.transaction_body_bytes is None:
            self.freeze_with(client)

        if self.operator_account_id is None:
            self.operator_account_id = client.operator_account_id

        # sign with operator's key if not already signed
        if not self.is_signed_by(client.operator_private_key.public_key()):
            self.sign(client.operator_private_key)

        transaction_proto = self.to_proto()
        response = self._execute_transaction(client, transaction_proto)

        return response

    def is_signed_by(self, public_key):
        """
        Checks if the transaction has been signed by the given public key.

        Args:
            public_key (PublicKey): The public key to check.

        Returns:
            bool: True if signed by the given public key, False otherwise.
        """
        public_key_bytes = public_key.public_bytes(
            encoding=Encoding.Raw,
            format=PublicFormat.Raw
        )

        for sig_pair in self.signature_map.sigPair:
            if sig_pair.pubKeyPrefix == public_key_bytes:
                return True
        return False

    def build_transaction_body(self):
        """
        Abstract method to build the transaction body.

        Subclasses must implement this method to construct the transaction-specific
        body and include it in the overall TransactionBody.

        Returns:
            TransactionBody: The protobuf TransactionBody message.

        Raises:
            NotImplementedError: Always, since subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must implement build_transaction_body()")
    
    def build_base_transaction_body(self):
        """
        Builds the base transaction body including common fields.

        Returns:
            TransactionBody: The protobuf TransactionBody message with common fields set.

        Raises:
            ValueError: If required IDs are not set.
        """
        if self.transaction_id is None:
            if self.operator_account_id is None:
                raise ValueError("Operator account ID is not set.")
            current_time = int(time.time())
            transaction_id = basic_types_pb2.TransactionID(
                accountID=self.operator_account_id.to_proto(),
                transactionValidStart=timestamp_pb2.Timestamp(seconds=current_time, nanos=0)
            )
        else:
            transaction_id = self.transaction_id 

        if self.node_account_id is None:
            raise ValueError("Node account ID is not set.")

        transaction_body = transaction_body_pb2.TransactionBody(
            transactionID=transaction_id,
            nodeAccountID=self.node_account_id.to_proto(),
            transactionFee=self.transaction_fee or self._default_transaction_fee,
            transactionValidDuration=duration_pb2.Duration(seconds=self.transaction_valid_duration),
            generateRecord=self.generate_record,
            memo=self.memo
        )

        return transaction_body

    def _execute_transaction(self, client, transaction_proto):
        """
        Abstract method to execute the transaction.

        Subclasses must implement this method to define how the transaction is sent
        to the network using the appropriate gRPC service.

        Args:
            client (Client): The client instance to use for execution.
            transaction_proto (Transaction): The protobuf Transaction message.

        Returns:
            TransactionReceipt or appropriate response based on transaction type.

        Raises:
            NotImplementedError: Always, since subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must implement _execute_transaction()")

    def _require_not_frozen(self):
        """
        Ensures the transaction is not frozen before allowing modifications.

        Raises:
            Exception: If the transaction has already been frozen.
        """
        if self.transaction_body_bytes is not None:
            raise Exception("Transaction is immutable; it has been frozen.")

    def set_transaction_memo(self, memo):
        """
        Sets the memo field for the transaction.

        Args:
            memo (str): The memo string to attach to the transaction.

        Returns:
            Transaction: The current transaction instance for method chaining.

        Raises:
            Exception: If the transaction has already been frozen.
        """
        self._require_not_frozen()
        self.memo = memo
        return self
