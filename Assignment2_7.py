# #  Write a program which accept one number and display below pattern

# Input : 5
# Output : 

#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5

def Display(iNo):

    if (iNo < 0):
        iNo = -iNo

    for x in range(iNo):

        for y in range(1,iNo + 1):
            print(y, end = " ")
        
        print()

def main():

    iValue = int(input("Enter number : "))

    Display(iValue)

if __name__ == '__main__':
    main()
