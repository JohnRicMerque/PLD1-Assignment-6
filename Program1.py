# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# Asking user for input 
def askFourNum():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    num3 = float(input("Enter 3rd number: "))
    num4 = float(input("Enter 4th number: "))
    return num1, num2, num3, num4

def highToLow(num1, num2, num3, num4):
    if num1>num2 and num1>num3 and num1>num4:
        if num2>num3 and num2>num4:
            if num3>num4:
                order = [num1, num2, num3, num4]
                return order
            else:
                order = [num1, num2, num4, num3]
                return order
        elif num3>num2 and num3>num4:
            if num2>num4:
                order = [num1, num3, num2, num4]
                return order
            else:
                order = [num1, num3, num4, num2]
                return order
        else:
            if num3>num2:
                order = [num1, num4, num3, num2]
                return order
            else:
                order = [num1, num4, num2, num3]
                return order
    
firstN, secondN, thirdN, fourthN = askFourNum()
numOrder = highToLow(firstN, secondN, thirdN, fourthN)
print(f" The order from highest to lowest is {numOrder}")