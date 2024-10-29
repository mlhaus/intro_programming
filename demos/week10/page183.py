
fruit = ["orange", "banana", "orange", "apple", "pineapple", "pear", "apple"]
print("Length of fruit:", len(fruit)) #7
print("Orange count:", fruit.count("orange")) #2
print("Banana count:", fruit.count("banana")) #1

unique_fruit = set(fruit) # remove duplicates
print("Unique fruit:", unique_fruit)
print("Unique fruit length:", len(unique_fruit)) #5

# Source: https://stackoverflow.com/questions/2587402/sorting-python-list-based-on-the-length-of-the-string
fruit2 = sorted(fruit, key=len) # sorted will return a copy of the original list sorted
print("Sorted fruit short to long:", fruit2) # will be sorted
# Source: https://stackoverflow.com/questions/4659524/how-to-sort-a-list-by-length-of-string-followed-by-reverse-alphabetical-order
fruit2 = sorted(fruit, key=len, reverse=True) # sorted will return a copy of the original list sorted
print("Sorted fruit long to short:", fruit2) # will be sorted
print("Original fruit:", fruit) # will not be sorted

fruit.sort(key=len) # sort will modify the original list
print("Sorted fruit short to long:", fruit)

fruit.sort() # You can sort lists, not sets
print("Sorted fruit A-Z:", fruit) # Order A-Z
fruit.reverse()
print("Sorted fruit Z-A:", fruit) # Order Z-A