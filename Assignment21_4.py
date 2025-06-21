# Design automation script which accept directory name and mail id from user and 
# create log file in that directory which contains information of running processes 
# as its name, PID, Username. After creating log file send that log file to the 
# specified mail.

# Usage: ProcInfoLog.py Demo Marvellousinfosystem@gmail.com

# Demo is name of Directory. marvellousinfosystem@gmail.com is the mail id.

import psutil
import os
import time
import sys
import smtplib
import email_validator
import email.message

def ProcessScan():

    List = []

    for proc in psutil.process_iter():
        info = proc.as_dict(['name', 'pid', 'username'])
        List.append(info)
    
    return List

def CheckEmail(Email):

    if(email_validator.validate_email(Email) == False):
        print("Plz provide a valid email id")
        exit()

def CreateLogFile(Dir, Email):

    timestamp = time.ctime()

    fname = "Marvellous_%s.log" %(timestamp)

    fname = fname.replace(" ", "_")
    fname = fname.replace(":", "__")

    Data = ProcessScan()

    if(os.path.exists(Dir) == False):
        os.mkdir(Dir)

    if(os.path.isabs(Dir) == False):
        Dir = os.path.abspath(Dir)

    fname = os.path.join(Dir, fname)

    fobj = open(fname, 'w')

    Border = '-'*83

    fobj.write(Border + "\n")
    fobj.write("This is a log file of MARVELLOUS AUTOMATION SCRIPT\n")
    fobj.write(Border + "\n\n")

    fobj.write("Total number of process running : "+ str(len(Data)))
    fobj.write("\nRunning Processes :\n")
    
    for value in Data:
        fobj.write("\n%s\n" %(value))

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("This file is created at \n" + timestamp + "\n")
    fobj.write(Border + "\n")

    print("File created with name ", {fname})

    fobj.close()

    SendMail(fname, Email)

def SendMail(fname, Email):

    sender = "ambraleamitt@gmail.com"
    password = "tzkmdxaptrzapaez"

    message = email.message.EmailMessage()
    message['Subject'] = 'Running Processes log file'
    message['From'] = sender
    message['To'] = Email

    fobj = open(fname, 'rb')
    data = fobj.read()
    fobj.close()

    fname = os.path.relpath(fname)

    message.add_attachment(data, maintype='application', subtype='octet-stream', filename = fname)
        
    sobj = smtplib.SMTP("smtp.gmail.com" , 587)
    sobj.starttls()
    sobj.login(sender, password)
    sobj.send_message(message)

    sobj.quit()
    
def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to create log file in given directory which contains information of running processes as its name, PID, Username & send the created log file to the give mail id")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  DirectoryName Email_ID") 
            print("Plz provide valid absolute path") 
    elif(len(sys.argv) == 3): 
        DirName = sys.argv[1]
        Email = sys.argv[2]
        CheckEmail(Email)

        CreateLogFile(DirName, Email)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
