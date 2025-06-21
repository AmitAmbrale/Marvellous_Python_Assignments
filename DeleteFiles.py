import os

def deleteFiles(List): 

    for value in List:
        os.remove(value)