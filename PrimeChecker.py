import threading
import multiprocessing
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

    def check_primes(self):
        results = []
        for num in self.numbers:
            results.append((num, self.is_prime(num)))
        return results

numbers = list(range(10_000, 12_000)) * 50
prime_checker = PrimeChecker(numbers)

def run_prime_check():
    prime_checker.check_primes()

def process_task():
    run_prime_check()

if __name__ == "__main__":
    thread_counts = [5, 10, 15]
    for count in thread_counts:
        threads = []
        start_time = time.time()
        for _ in range(count):
            t = threading.Thread(target=run_prime_check)
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        end_time = time.time()
        print(f"🧵 Threads: {count} | Time taken: {end_time - start_time:.4f} seconds")

    print("\n" + "-" * 50 + "\n")

    process_counts = [5, 10, 15]
    for count in process_counts:
        processes = []
        start_time = time.time()
        for _ in range(count):
            p = multiprocessing.Process(target=process_task)
            processes.append(p)
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        end_time = time.time()
        print(f"⚙️ Processes: {count} | Time taken: {end_time - start_time:.4f} seconds")
