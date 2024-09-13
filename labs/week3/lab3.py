#!/usr/bin/env python3

# Define all the hard-coded strings.
program_title = "*** Employment Application Program ***"
employee_id_prompt = "Please enter the employee ID: "
last_name_prompt = "Please enter the employee last name: "
first_name_prompt = "Please enter the employee first name: "
department_prompt = "Please enter the department name: "
salary_prompt = "Please enter the employee annual salary: "
table_name = "Employee Data"
emp_name_header = "EMPLOYEE NAME"
dept_header = "DEPARTMENT"
salary_header = "SALARY"
program_complete = "Program complete."

print(f"{program_title}")
# Prompt the user for input
first_name = input(first_name_prompt)
last_name = input(last_name_prompt)
department = input(department_prompt)
salary = float(input(salary_prompt))
salary = '${:,.2f}'.format(salary)
full_name = last_name + ', ' + first_name

table_width = 80
col1_width = int(table_width * .46)
col2_width = int(table_width * .24)
col3_width = int(table_width * .2)


# Display column titles
print(f'\n{table_name}')
print("-" * table_width)
# Use :< to left align, use :^ to center align, use :> to right align
print(f"| {emp_name_header:^{col1_width}} | {dept_header:^{col2_width}} | {salary_header:^{col3_width}} |")
print("-" * table_width)
print(f"| {full_name:<{col1_width}} | {department:<{col2_width}} | {salary:>{col3_width}} |")
print("-" * table_width)



print(f'\n{program_complete}\n')
