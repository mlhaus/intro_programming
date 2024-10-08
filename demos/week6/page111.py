# input parameters can have default values set
# These inputs are not required
def sum(n1 = 0, n2 = 0):
    # output is returned
    return n1 + n2

# When calling a function with default values, arguments are optional
print(sum()) # 0 + 0
print(sum(1)) # 1 + 0
print(sum(1, 2)) # 1 + 2
print(sum("Marc","Hauschildt")) # MarcHauschildt