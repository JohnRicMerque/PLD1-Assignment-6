# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random

# displays the addition question
def add(nums, itemNum):
    print(f"{itemNum + 1}. {nums[0]} + {nums[1]}")

# returns answer to the question
def getAnswer(nums):
    sum = nums[0] + nums[1]
    return sum

# generating two random numbers from 0 to 99
def random2():
    randomNums = random.sample(range(0, 99), 2)
    return randomNums

# asking user for answer and validating it
def userInput():
    while True:
        try:
            userInput = float(input("Enter your answer: "))
        except ValueError:
            print("Invalid Input. Please enter a number.")
            continue
        else:
            break
    return userInput

# checking
def check(rightAnswer, userAnswer):
    if rightAnswer == userAnswer:
        print("Your answer is CORRECT.")
        return 1
    else:
        print("Your answer is WRONG.") 
        return 0

# displaying the score
def displayScore(rightAnsNum,itemsNum):
    print("---------------------------------")
    print("RESULTS")
    print("---------------------------------")
    print(f"You got {rightAnsNum}/{itemsNum}")
    totalScorePercentage = int((rightAnsNum/itemsNum) * 100)
    print(f"Your percentage score is " + str(totalScorePercentage) + "%")

# program introduction
print("-------------------------------------")
print("Hello user, Welcome to Addition Quiz")
print("-------------------------------------")

# initial declaration of items and answers to 0
rightAnswers = 0
items = 0

# looping the process
while items != 10:
    twoNums = random2()
    question = add(twoNums, items)
    userAns = userInput()
    rightAns = getAnswer(twoNums)
    rightAnswers += check(rightAns, userAns)
    items += 1

# calling function to display scores
displayScore(rightAnswers, items)