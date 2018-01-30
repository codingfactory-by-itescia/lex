from block import Block
from pymongo import MongoClient


class Blockchain:

    def __init__(self):
        self.blocks = []
        self.create_genesis()

    def add_block(self, data):
        previous_block = self.blocks[len(self.blocks)-1]
        new_block = Block(data, previous_block.hash)
        self.blocks.append(new_block)

        client = MongoClient()
        db = client.blockchain 
        db.blocks.insert_one({
            "timestamp": new_block.timestamp,
            "data": new_block.data,
            "hash": new_block.hash,
            "previous_hash": new_block.previous_hash,
            "nounce": new_block.nounce
        })

    def create_genesis(self):
        new_genesis = Block("Genesis block", "0")
        self.blocks.append(new_genesis)
