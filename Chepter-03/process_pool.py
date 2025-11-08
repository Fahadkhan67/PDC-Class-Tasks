import multiprocessing
import random

class PrimeChecker:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

checker = PrimeChecker()

def check_prime(n):
    ok = checker.is_prime(n)
    return (n, ok)

if __name__ == "__main__":
    nums = [random.randint(10000, 20000) for _ in range(40)]
    pool = multiprocessing.Pool(processes=4)
    out = pool.map(check_prime, nums)

    pool.close()
    pool.join()

    print("Results:\n")
    for n, r in out:
        print(n, "prime" if r else "not prime")
