#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 999 to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = int(input("Enter test score: "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1 # adds 1 to the counter variable
    elif test_score == 999:
        break
    else:
        print("Test score must be from 0 through 100." +
        "Score discarded. Try again.")

# calculate average score
average_score = round(score_total / counter, 2)
                
# format and display the result
print("======================")
print(f"Total Score: {score_total}")
print(f"Average Score: {average_score}")
print()
print("Bye!")


