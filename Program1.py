# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# Asking user for input and validating it
def askFourNum():
    while True:
        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            num3 = float(input("Enter 3rd number: "))
            num4 = float(input("Enter 4th number: "))
        except ValueError:
            print("Invalid Input. Please enter a number.")
            continue
        else:
            break
    return num1, num2, num3, num4

# Function to arrange four numbers from highest to lowest
def highToLow(num1, num2, num3, num4):
    if num1 == num2 == num3 == num4:
        order = [num1, num2, num3, num4]
        return order

    # conditions if num1 is the largest
    if num1>=num2 and num1>=num3 and num1>=num4:
        if num2>=num3 and num2>=num4:
            if num3>=num4:
                order = [num1, num2, num3, num4]
                return order
            else:
                order = [num1, num2, num4, num3]
                return order
        elif num3>=num2 and num3>=num4:
            if num2>=num4:
                order = [num1, num3, num2, num4]
                return order
            else:
                order = [num1, num3, num4, num2]
                return order
        else:
            if num3>=num2:
                order = [num1, num4, num3, num2]
                return order
            else:
                order = [num1, num4, num2, num3]
                return order

    # conditions if num2 is the largest
    if num2>=num1 and num2>=num3 and num2>=num4:
        if num1>=num3 and num1>=num4:
            if num3>=num4:
                order = [num2, num1, num3, num4]
                return order
            else:
                order = [num2, num1, num4, num3]
                return order
        elif num3>=num1 and num3>=num4:
            if num2>=num4:
                order = [num2, num3, num2, num4]
                return order
            else:
                order = [num2, num3, num4, num2]
                return order
        else:
            if num3>=num2:
                order = [num2, num4, num3, num2]
                return order
            else:
                order = [num2, num4, num2, num3]
                return order
    
     # conditions if num3 is the largest
    if num3>=num1 and num3>=num2 and num3>=num4:
        if num1>=num2 and num1>=num4:
            if num2>=num4:
                order = [num3, num1, num2, num4]
                return order
            else:
                order = [num3, num1, num4, num2]
                return order
        elif num2>=num1 and num2>=num4:
            if num1>=num4:
                order = [num3, num2, num1, num4]
                return order
            else:
                order = [num3, num2, num4, num1]
                return order
        else:
            if num1>=num2:
                order = [num3, num4, num1, num2]
                return order
            else:
                order = [num3, num4, num2, num1]
                return order
    
     # conditions if num4 is the largest
    if num4>=num1 and num4>=num2 and num4>=num3:
        if num1>=num2 and num1>=num3:
            if num2>=num3:
                order = [num4, num1, num2, num3]
                return order
            else:
                order = [num4, num1, num3, num2]
                return order
        elif num2>=num1 and num2>=num3:
            if num1>=num3:
                order = [num4, num2, num1, num3]
                return order
            else:
                order = [num4, num2, num3, num1]
                return order
        else:
            if num1>=num2:
                order = [num4, num3, num1, num2]
                return order
            else:
                order = [num4, num3, num2, num1]
                return order
    
# Assigning input to multiple variables 
firstN, secondN, thirdN, fourthN = askFourNum()

# Calling the function
numOrder = highToLow(firstN, secondN, thirdN, fourthN)

# Display
print(f"The order from highest to lowest is {numOrder}")
