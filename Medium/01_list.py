fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# 1. Creating & Accessing Lists

my_list = [10, 20, 30, 40]

print(my_list[0])    # first element → 10
print(my_list[-1])   # last element → 40
print(my_list[1:3])  # slicing → [20, 30]

# 2. Updating Lists

my_list[1] = 25
print(my_list)   # [10, 25, 30, 40]
