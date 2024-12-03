"""
This is the main entry point for the blockchain application.
It demonstrates blockchain initialization, block addition, mining, transaction creation, 
and block hashing functionalities.
"""

from src.blockchain import Blockchain
from src.mining import proof_of_work
from src.transaction import Transaction
from src.utilities import hash_block

# Initialize the blockchain
blockchain = Blockchain()
"""
The Blockchain object is initialized to represent the main chain of blocks.
"""

# Add a new block
blockchain.add_block("This is the first block after Genesis")
"""
A new block is added to the blockchain with a custom message.
"""

# Display the blockchain
print("Blockchain:")
for block in blockchain.chain:
    print(block)
"""
The blockchain is printed, displaying each block in the chain.
"""

# Test mining functionality
last_proof = 0  # Example proof
"""
The proof from the previous block is initialized with a default value.
"""
new_proof = proof_of_work(last_proof)
"""
A new proof is generated using the proof-of-work algorithm.
"""
print(f"Last Proof: {last_proof}, New Proof: {new_proof}")
"""
The old and new proofs are displayed.
"""

# Test transaction creation
transaction = Transaction(sender="Alice", recipient="Bob", amount=100)
"""
A new transaction object is created with example sender, recipient, and amount values.
"""
print("Transaction:")
print(transaction.to_dict())
"""
The transaction is displayed in dictionary format.
"""

# Test block hashing
print("Hash of Genesis Block:")
print(hash_block(blockchain.chain[0]))
"""
The hash of the Genesis Block is calculated and displayed.
"""

if __name__ == "__main__":
    """
    Ensures that the script runs only when executed directly, not when imported as a module.
    """
    pass
