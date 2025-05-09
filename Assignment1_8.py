# Write a program which accept number from user and print that number of "*" on screen.

#    Input: 5
#    Output: * * * * *

def Display(iNo):

    for x in range(iNo):
        print("*", end = " ")

def main():
    
    print("Enter number :")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()