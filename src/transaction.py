# src/transaction.py
# This module defines the structure of a transaction.

class Transaction:
    def __init__(self, sender, recipient, amount):
        # Initialize a transaction with sender, recipient, and amount.
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        """Convert the transaction to a dictionary format."""
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
        }
