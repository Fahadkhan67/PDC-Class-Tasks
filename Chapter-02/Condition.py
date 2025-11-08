import threading
import time

class PrimeChecker:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

items = []
lock = threading.Condition()

MAX_SIZE = 20
TOTAL = 200

class Producer(threading.Thread):
    def run(self):
        for num in range(10_000, 10_000 + TOTAL):
            with lock:
                while len(items) == MAX_SIZE:
                    lock.wait()

                items.append(num)
                print(f"Produced: {num}")

                lock.notify_all()

            time.sleep(0.05)

class Consumer(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.checker = PrimeChecker()

    def run(self):
        while True:
            with lock:
                while not items:
                    lock.wait()

                num = items.pop(0)
                lock.notify_all()

            result = self.checker.is_prime(num)
            print(f"{self.name} checked {num} Prime: {result}")

            time.sleep(0.1)


def main():
    producer = Producer()
    consumer1 = Consumer("Worker-1")
    consumer2 = Consumer("Worker-2")

    producer.start()
    consumer1.start()
    consumer2.start()

    producer.join()
    print("Producer finished.")

if __name__ == "__main__":
    main()
