#  Design automation script which accept process name and display information 
#  of that process if it is running.

# Usage: ProcInfo.py Notepad

import psutil

def DisplayProcess(process):

    for proc in psutil.process_iter(['name']):
        
        if proc.info['name'] == process:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            print(info)

def main():

    process = input("Enter process name : ")

    DisplayProcess(process)

if __name__ == '__main__':
    main()
