# Print Pattern Using Recursion (Right Triangle)

# Write a recursive function to print the following pattern:

#    *
#    * *
#    * * *
#    * * * *
#    * * * * *

count = 1

def Display(row):

    global count

    if(row == 0):
        return 
    else:
        print("*" * count, end = " ")
        print()
        count = count + 1
        row = row - 1
        Display(row)

def main():

    iValue = int(input("Enter number : "))

    Display(iValue)

if __name__ == '__main__':
    main()
