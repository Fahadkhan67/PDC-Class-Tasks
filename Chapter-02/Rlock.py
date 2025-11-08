import threading
import time
import random

class Store:
    def __init__(self):
        self.lock = threading.RLock()
        self.data = []

    def add_number(self, n):
        with self.lock:
            self.data.append(n)

    def pop_number(self):
        with self.lock:
            if self.data:
                return self.data.pop(0)
            return None

class PrimeChecker:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def number_loader(box, count):
    print("Loading", count, "numbers")
    while count:
        n = random.randint(10000, 20000)
        box.add_number(n)
        print("Added", n)
        time.sleep(0.5)
        count -= 1

def number_checker(box, count):
    chk = PrimeChecker()
    print("Checking", count, "numbers")
    while count:
        num = box.pop_number()
        if num is None:
            time.sleep(0.2)
            continue
        res = chk.is_prime(num)
        print(num, "prime" if res else "not prime")
        time.sleep(0.4)
        count -= 1

def main():
    box = Store()
    load_count = random.randint(8, 15)
    check_count = random.randint(5, 12)

    t1 = threading.Thread(target=number_loader, args=(box, load_count))
    t2 = threading.Thread(target=number_checker, args=(box, check_count))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
