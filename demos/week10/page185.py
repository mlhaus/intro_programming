import random

fruit = ["orange", "banana", "bomb", "orange", "apple", "pineapple", "pear", "apple"]
print("Lowest fruit alpha:", min(fruit)) # apple
print("Highest fruit alpha:", max(fruit)) #pineapple
longest = max(fruit, key=len)
print("Longest fruit length:", longest)  # pineapple
shortest = min(fruit, key=len)
print("Shortest fruit length:", shortest)  # pear

random.shuffle(fruit)
print("Shuffled:",fruit)
random.shuffle(fruit)
print("Shuffled:",fruit)
random.shuffle(fruit)
print("Shuffled:",fruit)

count = 5
print(f"{count} random fruits")
for i in range(count):
    rand_fruit = random.choice(fruit)
    print(rand_fruit, end=" ")
print()