from hiero_sdk_python.transaction.transaction import Transaction
from hiero_sdk_python.hapi.services import token_pause_pb2
from hiero_sdk_python.response_code import ResponseCode

class TokenPauseValidator:
    """
    Validates prerequisites and constraints for a TokenPauseTransaction.
    """

    @staticmethod
    def validate_token_id(token_id):
        """
        Ensures a valid token ID was provided.
        
        Args:
            token_id (TokenId): The ID of the token to be paused.

        Raises:
            ValueError: If the token ID is not provided.
        """
        if not token_id:
            raise ValueError("Token ID is required for pausing a token.")
        
    @staticmethod
    def validate_token_pause(token_info):
        """
        Validate that the provided token can be paused.
        
        Args:
            token_info (TokenInfo): A structure containing metadata about the token
                                   (e.g. whether the token is deleted, paused, or
                                   has a pause key, etc.).

        Raises:
            ValueError: If the token is missing, already deleted, or has no valid pause key.
        """
        TokenPauseValidator._validate_token_not_deleted(token_info)
        TokenPauseValidator._validate_has_pause_key(token_info)
        # It is NOT an error if the token is already paused

    @staticmethod
    def _validate_token_not_deleted(token_info):
        """
        Ensures the token is not already deleted.

        Args:
            token_info (TokenInfo): Contains token metadata (including 'deleted' status).

        Raises:
            ValueError: If the token is marked deleted.
        """
        if getattr(token_info, "deleted", False):
            raise ValueError("Cannot pause a deleted token.")

    @staticmethod
    def _validate_has_pause_key(token_info):
        """
        Ensures the token has a valid pause key.

        Args:
            token_info (TokenInfo): Contains token metadata (including 'pause_key').

        Raises:
            ValueError: If the token has no pause key or the pause key is invalid/empty.
        """
        if not hasattr(token_info, "pause_key") or not token_info.pause_key:
            raise ValueError("Token has no valid pause key and cannot be paused.")
        

class TokenPauseTransaction(Transaction):
    """
    Represents a token pause transaction.

    This transaction pauses a specified token.

    Inherits from the base Transaction class and implements the required methods
    to build and execute a token pause transaction.
    """

    def __init__(self, token_id=None):
        """
        Initializes a new TokenPauseTransaction instance with optional token_id.

        Args:
            token_id (TokenId, optional): The ID of the token to be paused.
        """
        super().__init__()
        self.token_id = token_id
        self._default_transaction_fee = 3_000_000_000

    def set_token_id(self, token_id):
        self._require_not_frozen()
        self.token_id = token_id
        return self
    
    def build_transaction_body(self):
        """
        Builds and returns the protobuf transaction body for token pause.

        Returns:
            TransactionBody: The protobuf transaction body containing the token pause details.

        Raises:
            ValueError: If the token ID is missing.
        """

        # Validation checks
        TokenPauseValidator.validate_token_id(self.token_id)
        
        token_pause_body = token_pause_pb2.TokenPauseTransactionBody(
            token=self.token_id.to_proto(),
        )

        transaction_body = self.build_base_transaction_body()
        transaction_body.token_pause.CopyFrom(token_pause_body)

        return transaction_body

    def _execute_transaction(self, client, transaction_proto):
        """
        Executes the token pause transaction using the provided client.

        Args:
            client (Client): The client instance to use for execution.
            transaction_proto (Transaction): The protobuf Transaction message.

        Returns:
            TransactionReceipt: The receipt from the network after transaction execution.

        Raises:
            Exception: If the transaction submission fails or receives an error response.
        """
        # Retrieve token info and run pause-specific validations
        token_info = client.get_token_info(self.token_id)
        TokenPauseValidator.validate_token_pause(token_info)

        # Log if the token is already paused:
        if getattr(token_info, "paused", False):
            print("Token is already paused.")
            pass

        # Submit the token pause transaction
        response = client.token_stub.pauseToken(transaction_proto)

        if response.nodeTransactionPrecheckCode != ResponseCode.OK:
            error_code = response.nodeTransactionPrecheckCode
            error_message = ResponseCode.get_name(error_code)
            raise Exception(f"Error during transaction submission: {error_code} ({error_message})")

        receipt = self.get_receipt(client)
        return receipt
