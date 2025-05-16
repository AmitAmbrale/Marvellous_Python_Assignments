# Accept a list of numbers and use filter () to keep only even numbers.

# Expected Input:

# Enter list: 1 2 3 4 5 6

# Expected Output:

# Even numbers: [2, 4, 6]

Even = lambda iNo : (iNo % 2 == 0)

def filterX(Func, data):

    list = []

    for value in data:
        if(Func(value)):
            list.append(value)

    return list

def main():

    iValue = int(input("Enter size : "))

    data = []

    for x in range(iValue):
        no = int(input())
        data.append(no)
    
    FData = filterX(Even, data)

    print("Even numbers :", FData)

if __name__ == '__main__':
    main()