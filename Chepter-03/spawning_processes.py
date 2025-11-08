import multiprocessing

def myFunc(i):
    print(f"Calling myFunc from process number: {i}")
    for j in range(i):
        print(f"Output from myFunc: {j}")

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
