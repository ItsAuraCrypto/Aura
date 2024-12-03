"""
Short description of this module's purpose.

Detailed explanation about what this file does and its role in the project.
"""

# src/blockchain.py
# This module manages the blockchain and blocks.

class Blockchain:
    def __init__(self):
        # Initialize the blockchain with an empty chain and create the genesis block.
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain (Genesis Block)."""
        genesis_block = {"index": 0, "data": "Genesis Block"}
        self.chain.append(genesis_block)

    def add_block(self, data):
        """Add a new block to the blockchain."""
        block = {"index": len(self.chain), "data": data}
        self.chain.append(block)
