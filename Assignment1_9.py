# Write a program which display first 10 even numbers on screen.

# Output:

    # 2
    # 4
    # 6
    # 8
    # 10
    # 12
    # 14
    # 16
    # 18
    # 20


def Display(iNo):

    iNo *= 2

    for x in range(2, iNo + 1, 2):
        print(x, end = " ")

def main():

    print("Enter number :")
    iValue = int(input())
    
    Display(iValue)

if __name__ == "__main__":
    main()