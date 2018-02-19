from hashlib import sha256


class Proof:
    def __init__(self, block):
        self.block = block

    def run(self):
        self.data = self.block.previous_hash + self.block.transactions + self.block.timestamp
        self.nounce = 0
        self.hash = sha256((self.data + str(self.nounce)).encode()).hexdigest()

        while self.hash[:2] != "00":
            self.nounce += 1
            self.hash = sha256(
                (self.data + str(self.nounce)).encode()).hexdigest()

    def validate(self):
        current_hash = sha256(((self.block.previous_hash + self.block.transactions + self.block.timestamp) + str(self.block.nounce)).encode()).hexdigest()
        if self.block.hash == current_hash:
            return True
        return False
