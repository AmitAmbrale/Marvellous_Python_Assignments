# Power Function Using Recursion

# Write a recursive function to calculate x^n.

# power(2, 3)→8

product = 1

def Power(base, power):

    global product

    if (power <= 0):
        return 
    else:
        product = product * base
        power = power - 1
        Power(base, power)

def main():

    iValue1 = int(input("Enter base : "))
    iValue2 = int(input("Enter power : "))

    Power(iValue1, iValue2)

    print("Output : ", product)

if __name__ == '__main__':
    main()
