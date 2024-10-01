k = 5
m = 50

i = 1
q = 0
# this loop finds the first square greater than k
# 1 * 1 is not greater than 5
# 2 * 2 is not greater than 5
# 3 * 3 is greater than 5 (3 becomes the starting point)
while i * i < k:
    i += 1
# this loop counts the number of squares between k and m
while i * i < m:
    q += 1
    i += 1

print(q)

# def is_square(apositiveint):
#   x = apositiveint // 2
#   seen = set([x])
#   while x * x != apositiveint:
#     x = (x + (apositiveint // x)) // 2
#     if x in seen: return False
#     seen.add(x)
#   return True
#
# while k <= m:
#   if(is_square(k)):
#     q += 1
#   k += 1
# print(q)

