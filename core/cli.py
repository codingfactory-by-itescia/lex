import argparse

from blockchain import Blockchain

parser = argparse.ArgumentParser()
parser.add_argument("command", help="type of operation: add <data> or display")
parser.add_argument("--data", help="block data")

args = parser.parse_args()

blockchain = Blockchain()

if args.data: 
    if args.command == "add":
        blockchain.add_block(args.data)
        print("Done")

if args.command == "show":
    print("blockchain")