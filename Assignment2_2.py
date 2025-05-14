# 2. Write a program which accept one number and display below pattern.

# Input: 5

# Output:

#       * * * * *
#       * * * * *
#       * * * * *
#       * * * * *
#       * * * * *

def Display(iNo):
    
    if (iNo < 0):
        iNo = -iNo

    for x in range(iNo):

        for y in range(iNo):
            print("* ", end = "")
        
        print()

def main():

    iValue = int(input("Enter number : "))

    Display(iValue)

if __name__ == '__main__':
    main()
