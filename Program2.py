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

# asking user for answer
def userInput():
    userInput = float(input("Enter your answer: "))
    return userInput

# checking
def check(rightAnswer, userAnswer):
    if rightAnswer == userAnswer:
        return 1
    else: 
        return 0

# displaying the score
def displayScore(rightAnsNum,itemsNum):
    print("---------------------------------")
    print("RESULTS")
    print("---------------------------------")
    print(f"You got {rightAnsNum}/{itemsNum}")

# initial declaration of items and answers to 0
rightAnswers = 0
items = 0

# looping the process
while items != 10:
    twoNums = random2()
    question = add(twoNums)
    userAns = userInput()
    rightAns = getAnswer(twoNums)
    rightAnswers += check(rightAns, userAns)
    items += 1

# calling function to display scores
displayScore(rightAnswers, items)