import time
from backend.blockchain.blockchain import Blockchain
from backend.config import SECONDS

blockchain = Blockchain()
times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    mining_time = end_time - start_time
    times.append(mining_time)
    average_time = sum(times) / len(times)
    difficulty = blockchain.chain[-1].difficulty

    print(f'Mining time to add new block: {(mining_time / SECONDS)}s\n')
    print(f'Difficulty to add new block: {difficulty}\n')
    print(f'Average time to add blocks: {(average_time / SECONDS)}s\n')
    print('*********************************************\n\n')

