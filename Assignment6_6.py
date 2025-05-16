# Print Triangle Pattern using Nested loops
# Expected Output:

# *
# * *
# * * *
# * * * *
# * * * * *

def Display(iNo):

    for x in range(iNo):
        for y in range(x+1):
            print("* ", end = "")
        
        print()


def main():

    iValue = int(input("Enter input : "))

    Display(iValue)

if __name__ == '__main__':
    main()
