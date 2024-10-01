days_ran = int(input("how many days did you run this week? "))
for i in range(days_ran):
    print(i + 1)
print()

options = ["Add employee", "View employee", "View all employees", "Update employee", "Delete employee"]
for i in range(len(options)):
    print(f"{i + 1}) {options[i]}")
print()


# Adds 1 + 2 + 3 + 4
sum_of_numbers = 0
list = range(1, 5)
for i in list:
    sum_of_numbers += i
average_of_numbers = sum_of_numbers / len(list)
print("Sum:", sum_of_numbers)
print("Average:", average_of_numbers)
print()


# range(5, 0, -1) creates a list that starts with 5 and stops before 0, decreases by 1
# print 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i, end=" ")
print()


# range(1, 11, 2) creates a list that starts with 1 and stops before 11, increases by 2
# print 1, 3, 5, 7, 9
for i in range(1, 11, 2):
    print(i, end=" ")
print()

# range(1, 11) creates a list that starts with 1 and stops before 11
# print 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print()


# range(10) creates a list that starts with 0 and stops before 9
# print 0 to 9
for i in range(10):
    print(i, end=" ")
print()