import threading
import multiprocessing
import time
import random

class PrimeChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_primes(self):
        out = []
        for n in self.numbers:
            out.append((n, self.is_prime(n)))
        return out

numbers = list(range(10000, 12000)) * 50
checker = PrimeChecker(numbers)

sem = threading.Semaphore(0)
latest = None

def producer():
    global latest
    time.sleep(random.uniform(1, 2))
    latest = random.randint(1, 50)
    sem.release()

def consumer():
    sem.acquire()
    checker.check_primes()

def run_threads(c):
    ts = []
    start = time.time()
    for _ in range(c):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        ts.extend([t1, t2])
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    end = time.time()
    print(f"Threads {c} took {end - start:.4f}s")

def p_task():
    checker.check_primes()

def run_processes(c):
    ps = []
    start = time.time()
    for _ in range(c):
        p = multiprocessing.Process(target=p_task)
        ps.append(p)
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    end = time.time()
    print(f"Processes {c} took {end - start:.4f}s")

if __name__ == "__main__":
    for x in [5, 10, 15]:
        run_threads(x)
    print()
    for x in [5, 10, 15]:
        run_processes(x)
