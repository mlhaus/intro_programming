import copy

fruit = ["orange", "banana", "apple"]
fruit2 = fruit # shallow copy, fruit2 refers to the same list as fruit
fruit2[0] = "pineapple" # change orange to pineapple
print("Fruit:",fruit) # the original is affected with changes to a shallow copy

fruit3 = copy.deepcopy(fruit) # deep copy, fruit3 is independent of fruit
fruit3[0] = "pear"
print("Fruit3:",fruit3)
print("Fruit:",fruit) # the original is not affected with changes to a deep copy
print()

#slicing
numbers = [8,1,9,2,6,7,5,3]
print("List of numbers:",numbers)
print("First two numbers:",numbers[0:2])
print("First two numbers:",numbers[:2])
middle_index = len(numbers)//2
print("Middle number:",numbers[middle_index:middle_index+1])
print("Middle three numbers:",numbers[middle_index-1:middle_index+2])
print("Last two numbers:",numbers[-2:len(numbers) + 1])
print("Last two numbers:",numbers[-2:])

#concatenating
nums1 = [8,1,9]
nums2 = [2,6,7]
nums3 = nums1 + nums2
print(nums3)
nums1 += nums2
print(nums1)
