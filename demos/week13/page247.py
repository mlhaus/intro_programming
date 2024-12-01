import csv
lines = []
try:
    with open("sample2.txt", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row[0])
except FileNotFoundError as e:
    # This print if an error occurs
    print(e.strerror)
else:
    # This print if no error occurs
    print(lines)
finally:
    # This always prints
    print("Hello")
