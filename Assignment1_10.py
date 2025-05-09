# Write a program which accept name from user and display length of its name.

#    Input: Marvellous
#    Output: 10

def strlenX(str):
    
    length = len(str)
    
    return length


def main():
    
    str1 = str(input("Enter string : "))

    iRet = strlenX(str1)

    print("Length of '" + str1 + "' is :", iRet)

if __name__ == "__main__":
    main()