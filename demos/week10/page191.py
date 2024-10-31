from functools import reduce

numbers = [8,1,9,2,6,7]
fruit = ["banana", "orange", "apple", "pineapple", "grapes"]

def addTen(a):
    return a + 10

print(addTen(5))
# map() takes a list and converts it into a new list with modified values.
print(list(map(lambda a: a + 10, numbers)))
print(list(map(lambda a: a * 2, numbers)))
print(list(map(lambda fruit: fruit.upper(), fruit)))

# filter() takes a list and removes items to create a new list
# The lambda expression must be a boolean expression
# items in the list that match the expression are not removed
print(list(filter(lambda num: num % 2 == 0, numbers)))
print(list(filter(lambda fruit: fruit[0] == "o", list(filter(lambda fruit: len(fruit) == 6, fruit)))))
print(list(filter(lambda fruit: len(fruit) == 6 and fruit[0] == "o", fruit)))


# reduce() function takes a list and computes a single value from the list
sum = reduce(lambda a, b: a + b, numbers) # returns the sum of all numbers in a list
print(sum)

total = 0
for num in numbers:
    total += num
print(total)

print(sum/len(numbers)) # returns the average of all numbers in a list
print(total/len(numbers))










