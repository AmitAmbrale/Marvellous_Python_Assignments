# Create a Python program that uses multiprocessing.Pool to compute factorial of 
# numbers in a list.

import multiprocessing as mp

def Factorial(data):

    fact = 1

    for i in range(1,data+1):
        fact = fact * i

    return fact

def main():

    iValue = int(input("Enter number : "))

    data = list(range(1,iValue+1))

    p = mp.Pool()
    
    result = p.map(Factorial, data)

    p.close()
    p.join()

    print(result)

if __name__ == '__main__':
    main()
