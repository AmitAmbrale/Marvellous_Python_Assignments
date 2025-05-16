# Accept a list of integers from the user and use the map () function to double each value.

# Expected Input:
# Enter list : 1 2 3 4 5

# Expected Output:
# Doubled list : [2, 4, 6, 8, 10]

Double = lambda iNo : (iNo*2)

def mapX(Func, data):

    list = []

    for value in data:
        list.append(Func(value))

    return list

def main():

    iValue = int(input("Enter size : "))

    data = []

    for x in range(iValue):
        no = int(input())
        data.append(no)
    
    MData = mapX(Double, data)

    print("Doubled list :", MData)

if __name__ == '__main__':
    main()