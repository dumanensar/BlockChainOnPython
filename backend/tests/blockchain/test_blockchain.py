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

@pytest.fixture
def blockchain_three_blocks():
    blockchain = Blockchain()
    for i in range(3):
        blockchain.add_block(i)
    return blockchain


def test_is_valid_chain(blockchain_three_blocks):

    with pytest.raises(Exception, match='chain must have block'):
        Blockchain.is_valid_chain([])

    blockchain_three_blocks.chain[1].hash = 'evil_hash'

    with pytest.raises(Exception, match='must be formatted correctly'):
        Blockchain.is_valid_chain(blockchain_three_blocks.chain)

def test_is_valid_chain_bad_genesis(blockchain_three_blocks):
    blockchain_three_blocks.chain[0].data = 'evil'

    with pytest.raises(Exception, match='chain must start with the genesis block'):
        Blockchain.is_valid_chain(blockchain_three_blocks.chain)

def test_replace_chain(blockchain_three_blocks):
    blockchain = Blockchain()
    blockchain.replace_chain(blockchain_three_blocks.chain)
    assert blockchain.chain == blockchain_three_blocks.chain

def test_replace_cahin_no_longer(blockchain_three_blocks):
    blockchain = Blockchain()

    with pytest.raises(Exception, match='incoming chain must be longer than the local one'):
        blockchain_three_blocks.replace_chain(blockchain.chain)

def test_replace_cahin_invalid(blockchain_three_blocks):
    blockchain = Blockchain()

    blockchain_three_blocks.chain[1].hash = 'evil_hash'

    for index in range(0, len(blockchain_three_blocks.chain)):
        temp_chain = blockchain_three_blocks.chain[:]
        temp_chain[index].hash = 'evil_hash'

        with pytest.raises(Exception, match='incoming chain is invalid'):
            blockchain.replace_chain(temp_chain)

        

