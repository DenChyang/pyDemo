import time
from multiprocessing import Process

def test():
    while True:

        print("--1--")
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=test)
    p.start()
    # p.run()
    while 1:
        print("__main_212_")
        time.sleep(1)
