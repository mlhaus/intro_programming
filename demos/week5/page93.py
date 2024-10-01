# Display user message
print("\nWelcome to the average score program!\n")
# Define variables score_total and number_of_scores
score_total = 0
number_of_scores = 0
# Prompt the user for input
print("Enter 1 or more numbers from 0 to 100 [999 to stop]: ")
# Infinite loop
while(True):
#     get score
    score = float(input())
#     IF score is from 0 to 100
    if(score >= 0 and score <= 100):
#         add score to score total
        score_total += score
#         add 1 to number of scores
        number_of_scores += 1
#     ELSE IF score is 999
    elif(score == 999):
#         end loop
        break
#     ELSE
    else:
#         print error message
        print("Invalid entry.")
# Calculate average score
if(number_of_scores > 0):
    average_score = score_total / number_of_scores
    # Round average to 2 decimal places
    average_score = round(average_score, 2)
    # Display results
    print(f"Total: {score_total}")
    print(f"Count: {number_of_scores}")
    print(f"Average: {average_score}")
# Thank the user
print("Thanks for playing!")










