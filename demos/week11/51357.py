with open("numbers.txt", "r") as file:
    # Source: https://stackoverflow.com/a/20756176/6629315
    lines = file.read().splitlines()
if(len(lines) > 0):
    # Source: https://stackoverflow.com/a/7368801/6629315
    maxvalue = max(list(map(int, lines)))
print(maxvalue)