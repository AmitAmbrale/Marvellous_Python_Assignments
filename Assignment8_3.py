# Design python application which creates two threads as evenlist and oddlist. 
# Both the threads accept list of integers as parameter. Evenlist thread add all 
# even elements from input list and display the addition. Oddlist thread add all 
# odd elements from input list and display the addition.

import threading as th

def even(data):
    
    sum = 0
    
    for value in data:
        
        if (value % 2 == 0):
            sum = sum + value
            
    print("Addition of even elements :", sum)
    
def odd(data):
    
    sum = 0
    
    for value in data:
        
        if (value % 2 == 1):
            sum = sum + value 
            
    print("Addition of odd elements :", sum)

def main():
    
    iValue = int(input("Enter size : "))
    
    list = []
    
    for i in range(iValue):
        no = int(input())
        list.append(no)
    
    Evenlist = th.Thread(target = even, args = (list,))
    Oddlist = th.Thread(target = odd, args = (list,))
    
    Evenlist.start()
    Oddlist.start()
    
    Evenlist.join()
    Oddlist.join()
    
if __name__ == "__main__":
    main()    