# Create a file marks.txt with student name and marks. 
# Then read the file and display students who scored more than 75 marks.

def CreateFile(fname , data):

    fobj = open(fname, 'w')

    fobj.write("Names\tMarks\n")

    for i in range(0,len(data), 2):
        fobj.write(data[i])
        fobj.write('\t')
        fobj.write(str(data[i+1]))
        fobj.write("\n")
    
    fobj.close()   

def DisplayStudents(fname):

    fobj = open(fname, 'r')

    data = fobj.readline()

    while(len(data) > 0):
        data = fobj.readline()

        if (len(data) <= 0):
            break

        List = data.split()
        marks = int(List[1])

        if (marks >= 75):
            print("Name :", List[0], " Marks : ",List[1] )

    fobj.close()

def main():

    fname = "marks.txt"

    size = int(input("Enter number of students : "))

    List = []

    for i in range(size):
        name = input("Enter student name : ")
        marks = int(input("Enter amrks : "))
        List.append(name)
        List.append(marks)

    CreateFile(fname , List)

    DisplayStudents(fname)
    
if __name__ == '__main__':
    main()
