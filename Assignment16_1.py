# Write a Python program to create a text file named student.txt and write the names of 5 students into it.

import os 

def WriteName(data):

    fobj = open("student.txt", 'w')

    fobj.write("Names of student : \n")

    for i in range(len(data)):

        fobj.write(str(i+1) + ". ")
        fobj.write(data[i])
        fobj.write("\n")
    
    fobj.close()

def main():

    Names = []

    print("Enter names of 5 students :")
    for i in range(5):
        value = input()
        Names.append(value)
    
    WriteName(Names)

if __name__ == '__main__':
    main()
