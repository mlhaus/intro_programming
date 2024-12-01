filename = input("Enter filename: ")
movies = []
try:
    with open(filename, "w") as file:
        file.write("Hello\n")
        # for line in file:
        #     line = line.replace("\n", "")
        #     movies.append(line)
except FileNotFoundError as e:
    print(e.strerror)
except PermissionError as e:
    print(e.strerror)
