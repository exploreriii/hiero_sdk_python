from src.transaction.transaction import Transaction
from src.outputs import token_associate_pb2, transaction_body_pb2

class TokenAssociateTransaction(Transaction):
    def __init__(self):
        super().__init__()
        self.account_id = None
        self.token_ids = []

    def set_association_details(self, account_id, token_ids):
        """
        Setup method to initialize account ID and token IDs.
        """
        self.account_id = account_id
        self.token_ids = token_ids

    def build_transaction_body(self):
        """
        Build the TokenAssociate transaction body using the initialized details.
        """
        if not self.account_id or not self.token_ids:
            raise ValueError("Account ID and token IDs must be set")

        token_associate_tx_body = token_associate_pb2.TokenAssociateTransactionBody()
        token_associate_tx_body.account.CopyFrom(self.account_id.to_proto())
        token_associate_tx_body.tokens.extend([token_id.to_proto() for token_id in self.token_ids])

        return self.build_base_transaction_body(token_associate_tx_body)
