import blockchain


def main():
    chain = blockchain.Blockchain()
    chain.add_block("Bonjour")
    for b in chain.blocks:
        print("Data : " + b.data)
        print("Hash : " + b.hash)
        print("Previous_hash : " + b.previous_hash)


if __name__ == '__main__':
    main()
