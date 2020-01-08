
import time

def main():
    start_time = time.time()
    for a in range(0,1001):
        for b in range(0,1001):
            c = 1000 - a - b
            # for c in range(0,1001):
            if a+b+c == 1000 and a**2 +b**2  == c**2:
                print("%d,%d,%d"%(a,b,c))
    end_time = time.time()
    print("%s"%(end_time-start_time))

if __name__ == '__main__':
    main()
