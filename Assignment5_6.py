# Celsius to Fahrenheit Converter
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:

# F= (C x 9/5) + 32

# Expected Input:
# Enter temperature in Celsius: 25
# Expected Output: Temperature in Fahrenheit: 77.0°F

toFahrenheit = lambda temp : ((temp * 9/5) + 32)

def main():

    iValue = int(input("Enter temperature in Celsius : "))

    iRet = float(toFahrenheit(iValue))

    print("Temperature in Fahrenheit :", iRet ,end="°F")

if __name__ == '__main__':
    main()
