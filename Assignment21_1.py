# Design automation script which display information of running processes as 
# its name, PID, Username.

# Usage: ProcInfo.py

import psutil

def DisplayProcessInfo():

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            print(info)
        except Exception:
             print("Exception occurred")

def main():

    DisplayProcessInfo()

if __name__ == '__main__':
    main()