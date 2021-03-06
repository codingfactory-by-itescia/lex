from hashlib import sha256
from time import time

from proof import Proof


class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = str(time())
        proof = Proof(self)
        proof.run()
        self.hash = proof.hash
        self.nounce = proof.nounce
        self.tip = "true"
