# Write a function that accepts a string and checks whether it is a palindrome.

# Expected Input:
# Enter a string: radar

# Expected Output:
# radar is a palindrome.

def chkPalindrome(str):

    start = 0
    end = len(str) - 1
    temp = ''
    bFlag = True

    while(start <= end):

        if(str[start] != str[end]):
            bFlag = False
            break

        start += 1
        end -= 1

    return bFlag
    
def main():

    str = input("Enter a string : ")

    bRet = chkPalindrome(str)

    if(bRet):
        print(str,"is a palindrome.")
    else:
        print(str,"is not palindrome.")

if __name__ == '__main__':
    main()
