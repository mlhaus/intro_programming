def add_one(num):
    num += 1
    return num

def add_one_list(list):
    # This demonstration only works with count-controlled loops, not for-each loops
    for i in range(len(list)):
        list[i] += 1
    #return list # because lists are mutable, you don't have to return anything from a function that modifies a list.

def main():
    n = 10
    print(add_one(n)) # 11
    print(n) # 10, the variable n is immutable, meaning it does not change when passed to a function

    nums = [8, 1, 9, 2]
    print(add_one_list(nums)) # [9, 2, 10, 3]
    print(nums) # [9, 2, 10, 3], the list is mutable, meaning it changes when passed to a function

if __name__ == "__main__":
    main()