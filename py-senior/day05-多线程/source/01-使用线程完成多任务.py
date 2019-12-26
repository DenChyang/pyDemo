from threading import Thread
import time

#1. 如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是个的
def test():
    print("----昨晚喝多了，下次少喝点---")
    time.sleep(1)

if __name__ == '__main__':

    start_time = time.time()
    for i in range(5):
        print("=====================")
        t = Thread(target=test)
        t.start()
        print("%d"%i)
    end_time = time.time()
    print(end_time-start_time)
