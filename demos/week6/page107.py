# input parameters are variables placed inside the parenthesis
def sum(n1: float, n2: float) -> float:
    if(not isinstance(n1, int) and not isinstance(n1, float)):
        raise TypeError
    if (not isinstance(n2, int) and not isinstance(n2, float)):
        raise TypeError
    # output is returned
    return n1 + n2

# writing sum(1, 2) is calling the function, where 1 and 2 are arguments that get
# passed to the input parameter variables.
print(sum(1,2))
print(sum(3.25,5.5))
print(sum(-1,-2))
# print(sum("Marc","Hauschildt"))