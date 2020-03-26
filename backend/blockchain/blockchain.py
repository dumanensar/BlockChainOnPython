from backend.blockchain.block import Block
from backend.util.crypto_hash import crypto_hash

class Blockchain:
    """
    Blockchain: a ledger of transactions
    Implements a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain
        Enforce the following rules of the blockchain:
            - the chain must start with the genesis block
            - blocks must be formatted correctly
        """
        if len(chain) == 0:
            raise Exception("The chain must have block")
        
        first_block = chain[0]
        genesis_block = Block.genesis()

        if  first_block != genesis_block:
            raise Exception('The chain must start with the genesis block')
        
        try:
            for index in range(1, len(chain)):
                block = chain[index]
                last_block = chain[-1]
                Block.is_valid_block(last_block, block)            
        except Exception as e:
            raise Exception('Blocks must be formatted correctly')



def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    blockchain.add_block('three')
    blockchain.add_block('four')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()