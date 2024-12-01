# src/network.py
# This module manages the blockchain network and communication between nodes.

class Network:
    def __init__(self):
        # Initialize the network with an empty list of nodes.
        self.nodes = []

    def add_node(self, node):
        """Add a new node to the network."""
        self.nodes.append(node)

    def broadcast(self, data):
        """Broadcast data to all nodes in the network."""
        for node in self.nodes:
            print(f"Broadcasting data to node {node}: {data}")
