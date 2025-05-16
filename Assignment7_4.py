# Accept a list of numbers and use reduce() (from functools) to find the product of all numbers. I

# Expected Input:
# Enter list: 2 3 4

# Expected Output:
# Product : 24

from functools import reduce

Product = lambda iNo1, iNo2 : (iNo1 * iNo2)

def main():

    iValue = int(input("Enter size : "))

    data = []

    for x in range(iValue):
        no = int(input())
        data.append(no)
    
    RData = reduce(Product, data)

    print("Product :", RData)

if __name__ == '__main__':
    main()
