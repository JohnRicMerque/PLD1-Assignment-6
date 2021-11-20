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

firstN, secondN, thirdN, FourthN = askFourNum()