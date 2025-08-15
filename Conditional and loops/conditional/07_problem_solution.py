#Q7. Write a program to check whether a given year is a leap year or not
year = int(input("Enter a year: "))

# Leap year conditions:
# 1. Year should be divisible by 4
# 2. But if divisible by 100, it must also be divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year ✅")
else:
    print(f"{year} is NOT a Leap Year ❌")
