# append data to the end of the existing file
with open("spider.txt", "a") as file:
    file.write("\nThis is one of my favorite nursery rhymes")

# write mode will delete all existing data from a text file a new one
with open("spider.txt", "w") as file:
    file.write("Hello spider!")