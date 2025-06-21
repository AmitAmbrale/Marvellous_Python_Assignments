import os
from CheckFileSum import CheckSum

def WriteDuplicates(Dir):

    Count = 0

    if(os.path.exists(Dir) == False):
        print("No such directory present")
        exit()

    if(os.path.isdir(Dir) == False):
        print("Given input is not a direcctory")
        exit()

    if(os.path.isabs(Dir) == False):
        Dir = os.path.abspath(Dir)
    
    Dict = {}

    for FolderName, SubFolderNames, FileNames in os.walk(Dir):

        for fname in FileNames:
            
            fname = os.path.join(FolderName, fname)
            ChkSum = CheckSum(fname)
            Count += 1
            if(ChkSum in Dict):
                Dict[ChkSum].append(fname)
            else:
                Dict[ChkSum] = [fname]
    
    return Dict, Count