# Design python application which contains two threads named as thread1 and thread2. 
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. 
# After execution of thread1 gets completed then schedule thread2.

import threading as th

def forward():

    for i in range(51):
        print(i ,end = " ")
    
    print()

def backward():

    for i in range(50, 0, -1):
        print(i ,end = " ")

    print()

def main():

    Thread1 = th.Thread(target = forward)
    Thread2 = th.Thread(target = backward)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()