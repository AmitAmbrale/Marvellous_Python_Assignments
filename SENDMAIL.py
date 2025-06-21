import smtplib
import email.message as e
import os

def SendMail(fname, Email, FilesDeleted, FilesScanned, StartTime):

    sender = "ambraleamitt@gmail.com"
    password = "tzkmdxaptrzapaez"

    message = e.EmailMessage()
    message['Subject'] = "Deletion of duplicate files"
    message['From'] = sender
    message['To'] = Email
    time = "Starting time of scanning : " + str(StartTime)
    scan = "Total number of files scanned : " + str(FilesScanned)
    delete = "Total number of duplicate files found : " + str(FilesDeleted)
    message.set_content(time + "\n" + scan + "\n" + delete + "\n")

    fobj = open(fname, 'rb')
    data = ""
    data = fobj.read()
    fobj.close()

    fname = os.path.relpath(fname)

    message.add_attachment(data, maintype='application', subtype='octet-stream', filename = fname)
        
    sobj = smtplib.SMTP("smtp.gmail.com" , 587)
    sobj.starttls()
    sobj.login(sender, password)
    sobj.send_message(message)

    sobj.quit()