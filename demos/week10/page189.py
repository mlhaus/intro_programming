fruit_list = []
fruit_list.append("apple")
fruit_list.append("banana")
fruit_list.insert(0, "orange")
fruit_list.remove("banana")
fruit_list[0] = "pear"
print(fruit_list)
print(fruit_list[1:2]) # apple
fruit_tuple = ("orange", "apple", "banana")
# Tuples don't allow append, insert, remove, etc.
# fruit_tuple.append("apple")
# fruit_tuple.append("banana")
# fruit_tuple.insert(0, "orange")
# fruit_tuple.remove("banana")
# fruit_tuple[0] = "pear"
print(fruit_tuple)
print(fruit_tuple[1:2]) # apple

def get_weather():
    current_temp = 70
    percipition = 0
    cloud_coverage = .5
    return current_temp, percipition, cloud_coverage

weather = get_weather()
print(weather) # prints the values returned as a tuple
print("Current temp:", weather[0])
print("Percipition:", weather[1])
print("Cloud coverage:", weather[2])
# print("Unknown:", weather[3]) # Indexerror
# weather.append(0)
# weather[0] = 100










