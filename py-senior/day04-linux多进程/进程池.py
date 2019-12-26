from multiprocessing import Pool
import time
# import multiprocessing

def worker():
    for i in range(3):
        print("%d=="%i)
        time.sleep(2)


if __name__ == '__main__':
    po = Pool(3)
    for i in range(5):
        print("--main-- %d"%i)
        po.apply_async(worker)

    print("======start=====")
    po.close()
    po.join()
    print("======end=====")
