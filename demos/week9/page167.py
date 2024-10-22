bucket_of_candy = []
candy_eaten = []

bucket_of_candy.append("Twix")
bucket_of_candy.append("Snickers")
bucket_of_candy.append("M&Ms")
bucket_of_candy.remove("Snickers")# throw away Snickers
candy_eaten.append(bucket_of_candy.pop(0)) # Remove Twix and move it somewhere else
bucket_of_candy.insert(0, "Butterfinger") # append to the beginning
candy_eaten.append(bucket_of_candy.pop(bucket_of_candy.index("M&Ms")))
#candy_eaten.append(bucket_of_candy.pop(bucket_of_candy.index("Broccoli"))) # ValueError occurs if you try to remove something that doesn't exist

print("** Bucket Inventory **")
for i in range(len(bucket_of_candy)):
    print(bucket_of_candy[i])
print()

print("** In My Belly **")
for i in range(len(candy_eaten)):
    print(candy_eaten[i])
print()

