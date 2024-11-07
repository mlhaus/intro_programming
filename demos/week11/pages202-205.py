
# Read data
with open("spider.txt", "r") as file:
    print(file.read())
    

files = []
i = 1
while(True):
    file = open("spider.txt", "r")
    files.append(file)
    print(i)
    i += 1
    file.close() # The program crashes if too many file objects are open.
    # Use 'with open() as file' to automatically close files.