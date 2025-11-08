import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def with_barrier(sync, lock):
    name = multiprocessing.current_process().name
    sync.wait()
    num = random.randint(10000, 30000)
    result = is_prime(num)
    now = datetime.fromtimestamp(time())
    with lock:
        print(f"{name} | {num} prime: {result} | {now}")

def without_barrier():
    name = multiprocessing.current_process().name
    num = random.randint(10000, 30000)
    result = is_prime(num)
    now = datetime.fromtimestamp(time())
    print(f"{name} | {num} prime: {result} | {now}")

if __name__ == '__main__':
    sync = Barrier(2)
    lock = Lock()

    Process(name='p1-barrier', target=with_barrier, args=(sync, lock)).start()
    Process(name='p2-barrier', target=with_barrier, args=(sync, lock)).start()
    Process(name='p3-free', target=without_barrier).start()
    Process(name='p4-free', target=without_barrier).start()
