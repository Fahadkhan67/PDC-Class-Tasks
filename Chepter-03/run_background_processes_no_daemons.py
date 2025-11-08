import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}")
    
    if name == 'background_process':
        for i in range(5):
            print(f"{name}: {i}")
            time.sleep(0.5)
    else:
        for i in range(5, 10):
            print(f"{name}: {i}")
            time.sleep(0.5)
    
    print(f"Exiting {name}")

if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = False

    normal_process = multiprocessing.Process(
        name='normal_process',
        target=foo
    )
    normal_process.daemon = False

    background_process.start()
    normal_process.start()

    background_process.join()
    normal_process.join()
