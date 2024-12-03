"""
This module contains the Blockchain class, responsible for managing the blockchain and its blocks.
"""

class Blockchain:
    """
    Blockchain class to represent the structure and functionality of the blockchain.
    """

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block (genesis block) in the blockchain.
        """
        self.chain.append("Genesis Block")

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        """
        self.chain.append(data)
