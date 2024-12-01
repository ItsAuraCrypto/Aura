# src/blockchain.py
class Blockchain:
    def __init__(self):
        self.chain = []  
        self.create_genesis_block() 

    def create_genesis_block(self):
        genesis_block = {"index": 0, "data": "Genesis Block"}
        self.chain.append(genesis_block)

    def add_block(self, data):
        block = {"index": len(self.chain), "data": data}
        self.chain.append(block)
