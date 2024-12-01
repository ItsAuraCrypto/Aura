# src/mining.py
# This module handles the mining process (Proof of Work).

def proof_of_work(last_proof):
    """Simple Proof of Work algorithm to find a valid proof."""
    proof = 0
    while not is_valid_proof(last_proof, proof):
        proof += 1
    return proof

def is_valid_proof(last_proof, proof):
    """Validate the proof by ensuring it meets the difficulty criteria."""
    return (last_proof + proof) % 7 == 0  # Example validation
