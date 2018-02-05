import argparse

from blockchain import Blockchain
from iterator import Iterator

class CLI:
    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("command", help="type of operation: add <data> or show")
        parser.add_argument("--data", help="block data")

        args = parser.parse_args()

        blockchain = Blockchain()

        if args.data: 
            if args.command == "add":
                blockchain.add_block(args.data)
                print("Done")

        if args.command == "show":
            iterator = blockchain.iterator()
        

            while True:
                block = iterator.next()

                print("previous_hash : " + block['previous_hash'])
                print("current_hash : " + block['hash'])
                print("data : " + block['data'])
                print("timestamp : " + block['timestamp'])
                print("nounce : " + str(block['nounce']))
                print('\n')

                if block['previous_hash'] == "0":
                    break
                
                
                

