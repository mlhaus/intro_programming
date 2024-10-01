more = "y"
while more.lower() == "y":
    miles_driven = -1
    while miles_driven < 0:
        miles_driven = float(input("Enter miles driven: "))
    gallons_used = -1
    while gallons_used < 0:
        gallons_used = float(input("Enter gallons of gas used: "))
    mpg = round(miles_driven / gallons_used, 2)
    print(f"Miles per gallon: {mpg}")

    more = input("Continue? (y/n)")
print("Okay, bye!")



more = "y"
while more.lower() == "y":
    miles_driven = float(input("Enter miles driven: "))
    if miles_driven < 0:
        print("Entry must be greater than 0. Try again.")
        continue # restart the loop
    gallons_used = float(input("Enter gallons of gas used: "))
    if gallons_used < 0:
        print("Entry must be greater than 0. Try again.")
        continue  # restart the loop
    mpg = round(miles_driven / gallons_used, 2)
    print(f"Miles per gallon: {mpg}")

    more = input("Continue? (y/n)")
print("Okay, bye!")




print("Enter 'exit' when you're done.\n")
while True:
    data = input("Enter an integer to square: ")
    if(data.lower() == "exit"):
        break # end the loop
    i = int(data)
    print(f"{i} squared is {i * i}")
print("Okay, bye!")