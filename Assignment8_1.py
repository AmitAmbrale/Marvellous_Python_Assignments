# Design python application which creates two thread named as even and odd. 
# Even thread will display first 10 even numbers and odd thread will display 
# first 10 odd numbers.

import threading as th

def Display_Even():

    print("Even nos : ", end = "")

    for i in range(2, 21, 2):
        print(i, end = " ")
    
    print()

def Display_Odd():

    print("Odd nos : ", end = "")

    for i in range(1, 21, 2):
        print(i, end = " ")

    print()

def main():

    Even = th.Thread(target = Display_Even)
    Odd = th.Thread(target = Display_Odd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == '__main__':
    main()
