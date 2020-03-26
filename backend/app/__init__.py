from flask import Flask
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)

@app.route('/')
def default():
    return 'Welcome to the blockchain'

blockchain = Blockchain()

for i in range(3):
    blockchain.add_block(i)

@app.route('/blockchain')
def route_blockchain():
    return blockchain.__repr__()

app.run(port=5000)