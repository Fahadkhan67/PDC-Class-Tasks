import multiprocessing
import time
import random

class PrimeChecker:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def check_numbers():
    chk = PrimeChecker()
    nums = [random.randint(50000, 60000) for _ in range(10)]
    print("Process started\n")
    for n in nums:
        res = chk.is_prime(n)
        print(n, "prime" if res else "not prime")
        time.sleep(1)
    print("\nProcess finished")

if __name__ == "__main__":
    p = multiprocessing.Process(target=check_numbers)

    print("Before start:", p, p.is_alive())
    p.start()

    print("Running:", p, p.is_alive())
    time.sleep(3)

    p.terminate()
    print("Terminated:", p, p.is_alive())

    p.join()
    print("Joined:", p, p.is_alive())
    print("Exit code:", p.exitcode)
