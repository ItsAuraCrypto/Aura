"""
This module defines the structure and operations for blockchain transactions.
"""

# pylint: disable=too-few-public-methods
class Transaction:
    """
    Represents a blockchain transaction.
    """

    def __init__(self, sender, receiver, amount):
        """
        Initializes a transaction with sender, receiver, and amount details.

        Args:
            sender (str): The address of the sender.
            receiver (str): The address of the receiver.
            amount (float): The transaction amount.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
