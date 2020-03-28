import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-f4430e86-70e0-11ea-a7c4-5e95b827fd71'
pnconfig.publish_key = 'pub-c-7c1a202c-cb57-434d-a1c6-b435e6fd5d01'

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel {message_object.channel} Message: {message_object.message}')

class PubSub():
    """
    Handles the publish/subscribe layer of the application
    Provides communication between the nodes of the blockchain network.
    """
    
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()

def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, {'foo':'bar'})

if __name__ == '__main__':
    main()


