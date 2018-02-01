from block import Block
from pymongo import MongoClient

from iterator import Iterator


class Blockchain:

    def __init__(self):
        client = MongoClient()
        self.database = client.blockchain

        if self.database.blocks.count() == 0:
            self.create_genesis()

    def add_block(self, data):
        previous_block = self.database.blocks.find_one({"tip": "true"})
        self.database.blocks.update_one(
            {"tip": "true"}, {"$set": {"tip": "false"}})
        new_block = Block(data, previous_block['hash'])
        self.database.blocks.insert_one({
            "timestamp": new_block.timestamp,
            "data": new_block.data,
            "hash": new_block.hash,
            "previous_hash": new_block.previous_hash,
            "nounce": new_block.nounce,
            "tip": "true"
        })

    def create_genesis(self):
        new_genesis = Block("Genesis block", "0")
        self.database.blocks.insert_one({
            "timestamp": new_genesis.timestamp,
            "data": new_genesis.data,
            "hash": new_genesis.hash,
            "previous_hash": new_genesis.previous_hash,
            "nounce": new_genesis.nounce,
            "tip": "true"
        })

    def iterator(self):
        tip = self.database.blocks.find_one({"tip": "true"})
        return Iterator(tip.hash, self.database.blocks)
