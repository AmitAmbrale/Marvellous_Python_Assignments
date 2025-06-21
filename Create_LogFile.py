import time
import os

def createLogFile(Data, FileScan):

    timestamp = time.ctime()

    timestamp = timestamp.replace(" ", "_")
    timestamp = timestamp.replace(":", "__")

    fname = "Marvellous%s.log" %(timestamp)

    Dir = "Marvellous"

    if (os.path.exists(Dir) == False):
        os.mkdir(Dir)

    if(os.path.isabs(Dir) == False):
        Dir = os.path.abspath(Dir)

    fname = os.path.join(Dir, fname)

    fobj = open(fname, 'a')

    Border = '-'*83

    fobj.write(Border + "\n")
    fobj.write("This is a log file of MARVELLOUS AUTOMATION SCRIPT\n")
    fobj.write(Border + "\n")

    fobj.write("\nTotal number of scanned files :" + str(FileScan))
    fobj.write("\nTotal number deleted files :" + str(len(Data)))
    fobj.write("\nDeleted Files :\n")

    for value in Data:
        fobj.write(value)
        fobj.write("\n")

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("This file is created at \n" + str(time.ctime()) + "\n")
    fobj.write(Border + "\n")

    fobj.close()

    return fname