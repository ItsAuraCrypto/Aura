# src/node.py
# This module manages the node and its network connections.

class Node:
    def __init__(self, address):
        # Initialize the node with an address and an empty list of peers.
        self.address = address
        self.peers = []

    def connect_to_peer(self, peer_address):
        """Connect this node to another peer."""
        self.peers.append(peer_address)

    def broadcast(self, message):
        """Broadcast a message to all connected peers."""
        for peer in self.peers:
            print(f"Message sent to {peer}: {message}")
