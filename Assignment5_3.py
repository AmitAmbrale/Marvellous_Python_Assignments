# Voting Eligibility Checker
# Accept age from the user and check whether the person is eligible to vote. (Age should be 18 or above.)

# Expected Input:
# Enter age : 19
# Expected Output : Eligible to vote.

chkEligibilty = lambda iAge : (iAge >= 18)

def main():

    iValue = int(input("Enter age : "))

    bRet = chkEligibilty(iValue)

    if(bRet):
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

if __name__ == '__main__':
    main()
