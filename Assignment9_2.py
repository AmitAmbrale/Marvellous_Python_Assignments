# Write a Python program using multiprocessing. Process to square a 
# list of numbers using multiple processes.

import multiprocessing as mp

def Square(No):
    print(No * No)

def main():

    iSize = int(input("Enter size : "))

    list = []

    for i in range(iSize):
        no = int(input())
        list.append(no)

    for i in range(len(list)):
        p = mp.Process(target = Square, args = (list[i],))
        p.start()

if __name__ == "__main__":
    main()