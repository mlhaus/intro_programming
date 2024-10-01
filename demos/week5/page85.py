while(True):
    age = int(input("How old are you? "))
    if(age < 0 or age > 120):
        print("Invalid age")
    else:
        print(f"You are {age} years old")
        break

count = 0
while(count < 100):
    print(count, end=" ")
    count += 1
print()

choice = "y"
while choice.lower() == "y":
    print("Hello!")
    choice = input("Say hello again? (y/n): ")
print("Bye!")

age = 21
while(age >= 18):
    print("You can vote")
    voted = bool(input("Did you vote yet? ").lower() == "true")
    if(voted):
        break
print("Thanks for voting!")