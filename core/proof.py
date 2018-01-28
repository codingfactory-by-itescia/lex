from hashlib import sha256

class Proof:
    def __init__(self, block):
        self.block = block
        self.data = block.previous_hash + block.data + block.timestamp
        self.nounce = 0
        self.hash = sha256((self.data + str(self.nounce)).encode()).hexdigest()
        self.run()

    def run(self):
        while self.hash[:4] != "0000":
            print(self.hash)
            self.nounce += 1
            self.hash = sha256((self.data + str(self.nounce)).encode()).hexdigest()



