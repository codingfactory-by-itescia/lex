from block import Block
from pymongo import MongoClient

from iterator import Iterator


class Blockchain:

    def __init__(self):
        client = MongoClient()
        self.database = client.blockchain

        if self.database.blocks.count() == 0:
            self.create_genesis()

    def add_block(self, transactions):
        previous_block = self.database.blocks.find_one({"tip": "true"})
        self.database.blocks.update_one(
            {"tip": "true"}, {"$set": {"tip": "false"}})
        new_block = Block(transactions, previous_block['hash'])
        self.database.blocks.insert_one({
            "timestamp": new_block.timestamp,
            "transactions": new_block.transactions,
            "hash": new_block.hash,
            "previous_hash": new_block.previous_hash,
            "nounce": new_block.nounce,
            "tip": "true"
        })

    def create_genesis(self):
        tx = Transaction()
        new_genesis = Block(tx.new_coinbase(), None)
        self.database.blocks.insert_one({
            "timestamp": new_genesis.timestamp,
            "transactions": new_genesis.transactions,
            "hash": new_genesis.hash,
            "previous_hash": new_genesis.previous_hash,
            "nounce": new_genesis.nounce,
            "tip": "true"
        })

    def iterator(self):
        tip = self.database.blocks.find_one({"tip": "true"})
        return Iterator(self.database.blocks, tip['hash'])
