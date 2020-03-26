from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'foo'
    blockchain.add_block(data)
    block = blockchain.chain[-1]

    assert block.data == data
    assert block.last_hash == GENESIS_DATA['hash']
    
