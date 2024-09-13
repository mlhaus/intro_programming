name = input("What is your name? ")
print(f"Hello {name}!")
print("What is the current temperature in fahreheit?", end=" ")
temp_f = float(input())
temp_c = (temp_f - 32) * 5 / 9
print(f"It is {temp_c} degrees celsius!")