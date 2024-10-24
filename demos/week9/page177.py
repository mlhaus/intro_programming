student_colors = []
student_colors.append(["Max", "red"])
student_colors.append(["Tyson", "blue"])
student_colors.append(["Thor", "white"])
student_colors.append(["Charlotte", "black"])
student_colors.append(["Angel", "black"])
student_colors.append(["Colin", "pink"])
student_colors.insert(0, ["Chris", "green"])

print(student_colors) # multi-dimensional list

print(student_colors[0])
print(student_colors[1])
print(student_colors[2])
print(student_colors[3])
print(student_colors[4])
print(student_colors[5])
print(student_colors[6])
print()

# for-each enumeration
for i, student in enumerate(student_colors, start=1):
    print(f"#{i}) {student[0]}'s favorite color is {student[1]}")
print()

# for-each loop
for el in student_colors:
    print(f"{el[0]}'s favorite color is {el[1]}")
print()

# count-controlled loop
for i in range(len(student_colors)):
    # student_colors[i] represents an individual student list
    print(f"{student_colors[i][0]}'s favorite color is {student_colors[i][1]}")
print()


# Page 325 - Dictionaries

# Equivalent to [['Chris', 'green'], ['Max', 'red'], ['Tyson', 'blue'], ['Thor', 'white'],
# ['Charlotte', 'black'], ['Angel', 'black'], ['Colin', 'pink']]
student_colors_dict = {}
student_colors_dict["Chris"] = "green"
student_colors_dict["Max"] = "red"
student_colors_dict["Tyson"] = "blue"
student_colors_dict["Thor"] = "white"
student_colors_dict["Charlotte"] = "black"
student_colors_dict["Angel"] = "black"
student_colors_dict["Colin"] = "pink"
print(student_colors_dict)
for key, value in student_colors_dict.items():
    print(f"{key}'s favorite color is {value}")
print()

# Page 369 - Classes
class Person:
    # constructor
    def __init__(self, name, fav_color):
        self.name = name # attributes
        self.fav_color = fav_color # attributes
    # getter functions
    def get_name(self):
        return self.name;
    def get_fav_color(self):
        return self.fav_color


students = []
students.append(Person("Chris", "green"))
students.append(Person("Max", "red"))
students.append(Person("Tyson", "blue"))
students.append(Person("Thor", "white"))
students.append(Person("Charlotte", "black"))
students.append(Person("Angel", "black"))
students.append(Person("Colin", "pink"))
for s in students:
    print(f"{s.get_name()}'s favorite color is {s.get_fav_color()}")










