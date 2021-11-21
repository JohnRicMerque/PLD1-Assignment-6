# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random

# addition function
def add(nums):
    print(f"{nums[0]} + {nums[1]}")

# returns answer to the question
def getAnswer(nums):
    sum = nums[0] + nums[1]
    return sum

# generating random two numbers from 0 to 99
def random2():
    randomNums = random.sample(range(0, 99), 2)
    return randomNums

# program start
twoNums = random2()
question = add(twoNums)
rightAns = getAnswer(twoNums)
print(rightAns)