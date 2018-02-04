import argparse
from blockchain import Blockchain

parser = argparse.ArgumentParser(description='Creates a block')

parser.add_argument("addblock", metavar='command', help='')

args = parser.parse_args()

chain = Blockchain()
chain.add_block(args)
