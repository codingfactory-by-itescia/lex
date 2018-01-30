import blockchain
from proof import Proof


def main():
    chain = blockchain.Blockchain()
    chain.add_block("Hello World")


if __name__ == '__main__':
    main()
