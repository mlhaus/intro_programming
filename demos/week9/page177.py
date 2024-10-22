student_colors = []
student_colors.append(["Max", "red"])
student_colors.append(["Tyson", "blue"])
student_colors.append(["Thor", "white"])
student_colors.append(["Charlotte", "black"])
student_colors.append(["Angel", "black"])
student_colors.append(["Colin", "pink"])

print(student_colors) # multi-dimensional list

print(student_colors[0])
print(student_colors[1])
print(student_colors[2])
print(student_colors[3])
print(student_colors[4])
print(student_colors[5])
print()

# count-controlled loop
for i in range(len(student_colors)):
    # student_colors[i] represents an individual student list
    print(f"{student_colors[i][0]}'s favorite color is {student_colors[i][1]}")
print()

# for-each loop
for item in student_colors:
    print(f"{item[0]}'s favorite color is {item[1]}")
print()