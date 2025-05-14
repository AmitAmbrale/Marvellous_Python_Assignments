
def chkPrime(iNo):

    bFlag = True

    for x in range(2, int(iNo/2+1)):

        if(iNo % x == 0):
            bFlag = False
            break
    
    return bFlag

Sum = lambda iNo1, iNo2 : (iNo1 + iNo2)