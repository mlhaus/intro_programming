with open("data2.txt", "w") as file:
    with open("data1.txt", "r") as file2:
        line = file2.readline()
        while(line != "") :
            file.write(line)
            line = file2.readline()




