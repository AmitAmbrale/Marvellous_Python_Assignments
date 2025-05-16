# Vowel or Consonant Check

# Accept a single character from the user and check if it is a vowel (a, e, i, o, u). 
# If not, print it's a consonant.

# Expected Input:
# Enter a character: e
# Expected Output: 'e' is a vowel.

import msvcrt

def chkVowel(ch):

    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return True
    else:
        return False
    
def main():

    ch = ''

    ch = input("Enter a character : ")[0]

    bRet = chkVowel(ch)

    if(bRet):
        print(ch, "is vowel")
    else:
        print(ch, "is consonant")

if __name__ == '__main__':
    main()
