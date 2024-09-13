#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of gas used: "))

# calculate and round miles per gallon
mpg = round(miles_driven / gallons_used, 2)

# display the result
print()
print(f"Miles Per Gallon: {mpg}")
print()
print("Bye!")


