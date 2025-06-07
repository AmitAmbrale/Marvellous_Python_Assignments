# Print Numbers Using Recursion
# Write a recursive function to print numbers from 1 to N.
# Expected Output (for n=5):

# 1 2 3 4 5

count = 1

def Display(No):

    global count

    if (No < count):
        return 
    else:
        print(count, end = " ")
        count += 1
        Display(No)

def main():

    iValue = int(input("Enter number : "))

    Display(iValue)

if __name__ == "__main__":
    main()