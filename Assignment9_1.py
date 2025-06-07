# Create a Python program that starts 3 threads, each printing numbers from 1 to 5 
# with a delay of 1 second. Use threading.Thread.

import threading as th
import time as t

def Display():

    for i in range(6):
        print(i)
        t.sleep(1)

def main():

    Thread1 = th.Thread(target = Display)

    Thread2 = th.Thread(target = Display)

    Thread3 = th.Thread(target = Display)

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

if __name__ == '__main__':
    main()