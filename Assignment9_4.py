# Create a Python program that Compare execution time of summing numbers from 1 to 10 million 
# using normal function, threading, and multiprocessing.

import threading as th
import multiprocessing as mp
import time

def sum_normal():
    start = time.time()

    sum = 0

    for i in range(1, 10000001):
        sum = sum + i

    end = time.time()
    print("Normal Sum:", sum)
    print("Time required for normal function:", end - start)

def sum_thread():
    start = time.time()

    sum = 0

    for i in range(1, 10000001):
        sum = sum + i

    end = time.time()
    print("Threading Sum:", sum)
    print("Time required for threading:", end - start)

def sum_process():
    start = time.time()

    sum = 0

    for i in range(1, 10000001):
        sum = sum + i

    end = time.time()
    print("Multiprocessing Sum:", sum)
    print("Time required for multiprocessing:", end - start)

def main():
    print("Using normal function:")
    sum_normal()

    print("Using threading:")
    thread = th.Thread(target=sum_thread)
    thread.start()
    thread.join()

    print("Using multiprocessing:")
    process = mp.Process(target=sum_process)
    process.start()
    process.join()

if __name__ == '__main__':
    main()
