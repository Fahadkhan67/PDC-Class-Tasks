import multiprocessing
import random
import time

class PrimeChecker:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def run_task():
    name = multiprocessing.current_process().name
    print("Starting", name, "\n")
    nums = [random.randint(20000, 25000) for _ in range(5)]
    chk = PrimeChecker()
    for n in nums:
        r = chk.is_prime(n)
        print(name, "checked", n, "|", "prime" if r else "not prime")
        time.sleep(1)
    print("Ending", name, "\n")

if __name__ == "__main__":
    p1 = multiprocessing.Process(name="PrimeChecker A", target=run_task)
    p2 = multiprocessing.Process(target=run_task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
