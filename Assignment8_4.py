# Design python application which creates three threads as small, capital, digits. 
# All the threads accepts string as parameter. Small thread display number of small 
# characters, capital thread display number of capital characters and digits thread 
# display number of digits. Display id and name of each thread.

import threading as th

def smallCount(data):
    
    count = 0
    
    for i in range(len(data)):
        
        if (data[i] >= "a" and data[i] <= "z"):
            count += 1
            
    print("Number of small characters :", count)      
    
def capitalCount(data):
    
    count = 0
    
    for i in range(len(data)):
        
        if (data[i] >= "A" and data[i] <= "Z"):
            count += 1
            
    print("Number of capital characters :", count)   
    
def digitCount(data):
    
    count = 0
    
    for i in range(len(data)):
        
        if (data[i] >= "0" and data[i] <= "9"):
            count += 1
            
    print("Number of digits :", count)      
    

def main():
    
    str = input("Enter string : ")
    
    Small = th.Thread(target = smallCount, args = (str,))
    
    Capital = th.Thread(target = capitalCount, args = (str,))
    
    Digit = th.Thread(target = digitCount, args = (str,))
    
    Small.start()
    
    Capital.start()
    
    Digit.start()
    
    Small.join()
    
    Capital.join()
    
    Digit.join()
    
if __name__ == "__main__":
    main()    