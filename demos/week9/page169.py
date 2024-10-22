bucket_of_candy = ["Twix", "Peanut M&Ms", "Reese's PB Cups", "Butterfinger", "Snickers", "Skittles", "Starburst"]

# For-each loop
for item in bucket_of_candy:
    print(item)
print()

# Count-controlled for loop
for i in range(len(bucket_of_candy)):
    print(bucket_of_candy[i])
print()

scores = [88, -81, 92, 95, 66]
sum = 0
for item in scores:
    sum += item
average = sum / len(scores)
print("Scores:", scores)
print("Total:", sum)
print("Average:", average)
print("Highest:", max(scores))
print("Lowest:", min(scores))