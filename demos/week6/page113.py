def calc_tax(amount, tax_rate = 0.05):
    global tax # Allows you to not use return statements
    tax = amount * tax_rate

tax = 0
calc_tax(100)
print(tax)
calc_tax(100, .07) # don't print if there is not a return statement
print(tax)