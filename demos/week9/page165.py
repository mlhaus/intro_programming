personal_info = ["Marc", "Hauschildt", 43, 190.5]
for i in range(len(personal_info)):
    print(personal_info[i])
print()


temps = [78, 66, 81, 80, 69, 72, 75]
for i in range(len(temps)):
    print(temps[i])
print()

candy = ["Twix", "Peanut M&Ms", "Reese's PB Cups", "Butterfinger", "Snickers", "Skittles", "Starburst"]

# modify a list item by assigning a new value to its index
candy[1] = "Carmel M&Ms"

for i in range(len(candy)):
    print(candy[i])
print()

print(candy[0])
print(candy[1])
print(candy[2])
print(candy[3])
print(candy[4])
print(candy[5])
print(candy[6])
#print(candy[7]) # index doesn't exist
print()


# Accesses values in reverse order
for i in range(-1, len(candy) * -1 - 1, -1):
    print(candy[i])
print()

print(candy[-1])
print(candy[-2])
print(candy[-3])
print(candy[-4])
print(candy[-5])
print(candy[-6])
print(candy[-7])
print()



candy1 = "Twix"
candy2 = "Peanut M&Ms"
candy3 = "Reese's PB Cups"
candy4 = "Butterfinger"
candy5 = "Snickers"
print(candy1)
print(candy2)
print(candy3)
print(candy4)
print(candy5)
print()

# the range function returns a list of integers
# In this example, [0,1,2,3,4,5,6,7,8,9]
print(list(range(10)))

# prints 0-9
for i in range(10):
    print(i, end=" ")
print()