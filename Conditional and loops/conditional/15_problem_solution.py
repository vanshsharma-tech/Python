# Q15. Check divisibility by 3, 5, both, or neither.

number = int(
    input("Enter your number to check divisibility by 3, 5, both, or neither: ")
)

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by 3, 5, both")
elif number % 3 == 0:
    print(f"{number} is divisible by 3 only")
elif number % 5 == 0:
    print(f"{number} is divisible by 5 only")
else:
    print(f"{number} is not divisible by 3 or 5")
