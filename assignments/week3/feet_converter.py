#!/usr/bin/env python3
'''
Name: feet_converter.py
Date: 2024-09-26
Author: Marc Hauschildt
Description: Prompt user for feet, display 3 conversions
'''

# Define all the hard-coded strings.
program_title = "*** Feet Converter Program ***"
feet_prompt = "Enter number of feet: "
table_name = "Conversion Data"
cm_header = "Centimeters"
in_header = "Inches"
m_header = "Meters"
program_complete = "Program complete."

print(f"{program_title}")
# Prompt the user for input
feet = float(input(feet_prompt))

cm = feet * 30.48
inch = feet * 12
m = feet * 0.3048

table_width = 80
col1_width = int(table_width * .3)
col2_width = int(table_width * .3)
col3_width = int(table_width * .3)


# Display column titles
print(f'\n{table_name}')
print("-" * table_width)
# Use :< to left align, use :^ to center align, use :> to right align
print(f"| {cm_header:^{col1_width}} | {in_header:^{col2_width}} | {m_header:^{col3_width}} |")
print("-" * table_width)
print(f"| {cm:>{col1_width},.3f} | {inch:>{col2_width},.3f} | {m:>{col3_width},.3f} |")
print("-" * table_width)



print(f'\n{program_complete}\n')
