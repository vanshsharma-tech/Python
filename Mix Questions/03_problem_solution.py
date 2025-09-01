#  Add two numbers entered by the user without using + operator.

# ✅ Method 1: Using sum()

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("Sum =",sum([num1,num2]))


# ✅ Method 2: Using operator.add()

import operator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# print("Sum =", operator.add(a, b))
