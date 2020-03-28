import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNReconnectionPolicy
from backend.blockchain.block import Block
from backend.blockchain.blockchain import Blockchain

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-f4430e86-70e0-11ea-a7c4-5e95b827fd71'
pnconfig.publish_key = 'pub-c-7c1a202c-cb57-434d-a1c6-b435e6fd5d01'
pnconfig.reconnect_policy = PNReconnectionPolicy.LINEAR

CHANNELS = {
    'TEST' :'TEST',
    'BLOCK' :'BLOCK'
}

class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self, pubnub, message_object):
        print(f'\n-- Channel {message_object.channel} Message: {message_object.message}')

        channel = message_object.channel
        message = message_object.message

        if channel == CHANNELS['BLOCK']:
            block = Block.from_json(message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)
            try:
                self.blockchain.replace_chain(potential_chain)
                print('Blockchain is changed')
            except Exception as e:
                print(f'Blockchain is not changed: {e}')


class PubSub():
    """
    Handles the publish/subscribe layer of the application
    Provides communication between the nodes of the blockchain network.
    """
    
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())


def main():
    blockchain = Blockchain()
    pubsub = PubSub(blockchain)
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], {'foo':'bar'})

if __name__ == '__main__':
    main()


