from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA
import pytest

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

def test_is_valid_chain():

    with pytest.raises(Exception, match='chain must have block'):
        Blockchain.is_valid_chain([])

    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.chain[1].hash = 'evil_hash'

    with pytest.raises(Exception, match='must be formatted correctly'):
        Blockchain.is_valid_chain(blockchain.chain)

    blockchain = Blockchain()
    blockchain.chain[0].data = 'evil'

    with pytest.raises(Exception, match='chain must start with the genesis block'):
        Blockchain.is_valid_chain(blockchain.chain)
        

