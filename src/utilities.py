# src/utilities.py
# This module provides general utility functions.

import hashlib

def hash_block(block):
    """Generate a SHA-256 hash for a block."""
    block_string = str(block).encode()
    return hashlib.sha256(block_string).hexdigest()
