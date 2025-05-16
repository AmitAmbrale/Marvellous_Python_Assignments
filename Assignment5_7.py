# Area and Perimeter of Rectangle
# Accept the length and width of a rectangle. Calculate and display the area and perimeter.

# Perimeter: 2 * (length (l) + width (w)) or P = 2l + 2w. 
# Area: length (l) * width (w) or A = lw. 

# Expected Input:
# Enter length: 5
# Enter width: 3

# Expected Output:
# Area: 15
# Perimeter: 16

Area = lambda iNo1, iNo2 : (iNo1*iNo2)

Perimeter = lambda iNo1, iNo2 : (2*(iNo1 + iNo2))

def main():

    iValue1 = int(input("Enter length : "))
    iValue2 = int(input("Enter width : "))

    iRet = Area(iValue1, iValue2)

    print("Area :", iRet)

    iRet = Perimeter(iValue1, iValue2)

    print("Perimeter :", iRet)

if __name__ == '__main__':
    main()
