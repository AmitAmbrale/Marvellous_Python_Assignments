# Design python application which creates two threads as evenfactor and oddfactor. 
# Both the thread accept one parameter as integer. Evenfactor thread will display 
# addition of even factors of given number and oddfactor will display addition of odd 
# factors of given number. After execution of both the thread gets completed main thread 
# should display message as "exit from main".

import threading as th

def evenFactor(No):
    
    sum = 0
    
    for i in range(1, int(No/2 + 1)):
        
        if (No % i == 0) and (i % 2 == 0):
            sum = sum + i
            
    print("Addition of even factors:", sum)
    
def oddFactor(No):
    
    sum = 0
    
    for i in range(1, int(No/2 + 1)):
        
        if (No % i == 0) and (i % 2 == 1):
            sum = sum + i
            
    print("Addition of odd factors:", sum)

def main():
    
    iValue = int(input("Enter number : "))
    
    Even_Factor = th.Thread(target = evenFactor, args = (iValue,))
    Odd_Factor = th.Thread(target = oddFactor, args = (iValue,))
    
    Even_Factor.start()
    Odd_Factor.start()
    
    print("exit from main")
    
    
if __name__ == "__main__":
    main()    