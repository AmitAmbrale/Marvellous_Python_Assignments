
def Add(iNo1, iNo2):
    
    iAns = 0

    iAns = iNo1 + iNo2

    return iAns

def Sub(iNo1, iNo2):
    iAns = 0

    iAns = iNo1 - iNo2

    return iAns

def Mul(iNo1, iNo2):
    iAns = 0

    iAns = iNo1 * iNo2

    return iAns

def Div(iNo1, iNo2):
    iAns = 0

    if (iNo2 == 0):
        print("Error in Division : Enter a non zero number")
        return -1

    iAns = iNo1 / iNo2

    return iAns