"""
This is the main script for the Aura project.
It initializes the blockchain, tests mining, transactions, and other functionalities.
"""

from src.blockchain import Blockchain
from src.mining import proof_of_work
from src.transaction import Transaction
from src.utilities import hash_block

# Initialize the blockchain
blockchain = Blockchain()

# Add a new block
blockchain.add_block("This is the first block after Genesis")

# Display the blockchain
print("Blockchain:")
for block in blockchain.chain:
    print(block)

# Test mining functionality
LAST_PROOF = 0  # Example proof
NEW_PROOF = proof_of_work(LAST_PROOF)
print(f"Last Proof: {LAST_PROOF}, New Proof: {NEW_PROOF}")

# Test transaction creation
transaction = Transaction(sender="Alice", recipient="Bob", amount=100)
print("Transaction:")
print(transaction.to_dict())

# Test block hashing
print("Hash of Genesis Block:")
print(hash_block(blockchain.chain[0]))
