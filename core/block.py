from hashlib import sha256
from time import time


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.set_hash()

    def set_hash(self):
        timestamp = time()
        headers = self.previous_hash + self.data + timestamp 
        self.hash = sha256(headers.encode()).hexdigest()
