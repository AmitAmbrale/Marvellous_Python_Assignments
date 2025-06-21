# Accept 10 numbers from the user and write them into a file named 
# numbers.txt, each on a new line.

def WriteNumbers(data):

    fname = "numbers.txt"

    fobj = open(fname, 'w')

    fobj.write("Numbers : \n")

    for i in range(len(data)):

        fobj.write(str(i+1) + ". ")
        fobj.write(str(data[i]))
        fobj.write("\n")
    
    fobj.close()

def main():

    Data = []

    print("Enter 10 numbers : ")

    for i in range(10):
        no = int(input())
        Data.append(no)

    WriteNumbers(Data)

if __name__ == '__main__':
    main()
