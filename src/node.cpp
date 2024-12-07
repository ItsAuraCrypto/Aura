"""
This module represents a node in the blockchain network.
"""

class Node:
    """
    Represents a single node in the blockchain network.
    """

    def __init__(self, address):
        """
        Initializes the node with a unique address.

        Args:
            address (str): The node's unique address.
        """
        self.address = address
        self.blockchain = None

    def connect_to_network(self):
        """
        Connects the node to the blockchain network.
        """
        pass
