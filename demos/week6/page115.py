def cToF(temp):
    return temp * 9 / 5 + 32

def fToC(temp):
    return (temp - 32) * 5 / 9

# Print f to c (0, 40, 80, 120, 160, 200)
for temp in range(0, 212, 40):
    print(f"{temp}\N{DEGREE SIGN}f = {round(fToC(temp), 1)}\N{DEGREE SIGN}c")
print()
# Print c to f (0, 20, 40, 60, 80, 100)
for temp in range(0, 101, 20):
    print(f"{temp}\N{DEGREE SIGN}c = {round(cToF(temp), 1)}\N{DEGREE SIGN}f")