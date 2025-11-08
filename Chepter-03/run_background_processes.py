import multiprocessing
import time

def run_task():
    name = multiprocessing.current_process().name
    print(f"Starting {name}")
    if name == "daemon_worker":
        for i in range(5):
            print(f"{name}: {i}")
            time.sleep(0.3)
    else:
        for i in range(5, 10):
            print(f"{name}: {i}")
            time.sleep(0.3)
    print(f"Ending {name}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(name="daemon_worker", target=run_task)
    p1.daemon = True

    p2 = multiprocessing.Process(name="normal_worker", target=run_task)
    p2.daemon = False

    p1.start()
    p2.start()

    p2.join()
    time.sleep(1)
