import threading
import time

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

def worker(thread_id, numbers_chunk, results, lock):
    print(f"Thread {thread_id} started.")
    local_results = []
    for num in numbers_chunk:
        local_results.append((num, PrimeChecker([]).is_prime(num)))
    with lock:
        results.extend(local_results)
    print(f"Thread {thread_id} finished.")

if __name__ == "__main__":
    numbers = list(range(10_000, 10_050))  # small chunk for demonstration
    num_threads = 4
    chunk_size = len(numbers) // num_threads
    threads = []
    results = []
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(i+1, numbers[start:end], results, lock))
        threads.append(t)
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()

    for num, is_p in results:
        print(f"{num} is prime: {is_p}")

    print("\nTotal primes found:", sum(1 for _, p in results if p))
