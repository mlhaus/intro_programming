#!/usr/bin/env python3
import sys
# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:         "))
if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
    sys.exit()
gallons_used = float(input("Enter gallons of gas used:  "))
if gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
    sys.exit()

# calculate and display miles per gallon
mpg = round(miles_driven / gallons_used, 1)
print("Miles Per Gallon:          ", mpg)

print()
print("Bye!")



