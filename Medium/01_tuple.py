# 🔗 Tuple in Python
# 🔹 What is a Tuple?

# A tuple is an ordered, immutable (unchangeable) collection in Python.

# It can hold different data types like integers, strings, lists, or even dictionaries.

# Defined using () (parentheses).

my_tuple = (10, 20, 30, 40)
mixed = (1, "hello", 3.14, True)

# Creating Tuples

t1 = (1, 2, 3)       # normal tuple
t2 = (1,)            # single element tuple (comma is important)
t3 = tuple([4, 5, 6])  # using tuple() function

# Accessing Elements

nums = (10, 20, 30, 40)

print(nums[0])      # 10
print(nums[-1])     # 40
print(nums[1:3])    # (20, 30)

nums = (10, 20, 30)
# nums[1] = 50   ❌ Error (cannot change values)

# But you can convert tuple → list → modify → tuple again:

nums = (10, 20, 30)
temp = list(nums)
temp[1] = 50
nums = tuple(temp)
print(nums)   # (10, 50, 30)
