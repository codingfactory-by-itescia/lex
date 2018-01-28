from block import Block


class Blockchain:
    def __init__(self):
        self.blocks = []
        self.create_genesis()

    def add_block(self, data):
        previous_block = self.blocks[len(self.blocks)-1]
        new_block = Block(data, previous_block.hash)
        self.blocks.append(new_block)

    def create_genesis(self):
        new_genesis = Block("Genesis block", "0")
        self.blocks.append(new_genesis)
