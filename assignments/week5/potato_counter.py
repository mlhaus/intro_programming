from user_input import get_int

print("Welcome to the Potato Peeler Program")
total_potatoes = 0
number_of_sacks = get_int("How many sacks of potatoes need to be peeled?", True, 1)
for i in range(1, number_of_sacks + 1):
    num_potatoes = get_int(f"How many potatoes are in sack {i}?", True, 0)
    total_potatoes += num_potatoes
    for j in range(1, num_potatoes + 1):
        print(f"Peeling potato {j} from sack {i}")
try:
    average = round(total_potatoes / number_of_sacks, 2)
    print(f"Total Potatoes peeled: {total_potatoes}")
    print(f"Number of Sacks: {number_of_sacks}")
    print(f"Average Potatoes Per Sack: {average}")
    print("Thank you for playing!")
except ZeroDivisionError:
    print("Cannot be zero")
