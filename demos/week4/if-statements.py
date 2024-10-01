purchase_amt = float(input("Enter purchase amount: "))
# A company offers Retail customers 20% discount on orders $250+, 10% on orders 100+, otherwise no discount
# They also offer Wholesale customers 50% discount on orders $500+, 40% on anything else.
customer_type = input("Enter customer type [Retail or Wholesale]: ").lower()
if(customer_type == "retail" or customer_type == "wholesale"):
    if(customer_type == "retail"):
        if(purchase_amt >= 250):
            discount_percent = .2
        elif(purchase_amt >= 100):
            discount_percent = .1
        else:
            discount_percent = 0
    else:
        if (purchase_amt >= 500):
            discount_percent = .5
        else:
            discount_percent = .4
else:
    print("Invalid customer type")

purchase_amt = purchase_amt * (1 - discount_percent)
print(f"Please pay {purchase_amt}")


# A company offers a 20% discount on orders $500+, 10% on orders 250+, otherwise no discount

if(purchase_amt >= 500):
    discount_percent = .2
elif(purchase_amt >= 250):
    discount_percent = .1
else:
    discount_percent = 0

purchase_amt = purchase_amt * (1 - discount_percent)
print(f"Please pay {purchase_amt}")


score = 95
if(score < 0 or score > 100):
    print("Invalid score")

# 90-100 A, 80-89 B, 70-79 C, 60-69 D, 0-59 F
if(score >= 90 and score <= 100):
    print("A")
elif(score >= 80 and score < 90):
    print("B")
elif(score >= 70 and score < 80):
    print("C")
elif(score >= 60 and score < 70):
    print("D")
elif(score >= 0 and score <= 60):
    print("F")
else:
    print("Invalid score")

if(score >= 90):
    print("A")
elif(score >= 80):
    print("B")
elif(score >= 70):
    print("C")
elif(score >= 60):
    print("D")
else:
    print("F")


if(score >= 90):
    print("A")
if(score >= 80):
    print("B")
if(score >= 70):
    print("C")
if(score >= 60):
    print("D")
if (score >= 0):
    print("F")



if(score < 60):
    print("F")
elif(score < 70):
    print("D")
elif(score < 80):
    print("C")
elif(score < 90):
    print("B")
else:
    print("A")




age = 21
# A boolean expression (True or False) must come after the if statement, and it must end with a colon,
# and there must be at least one indented line.
if(age >= 18):
    print("You may vote")
else:
    print("You are too young to vote")



