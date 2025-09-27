# Q9. ✖️ Find the factorial of a number using recursion, not loops.


def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return "Please Enter the valid number"

    return num * factorial(num - 1)


number = int(input("Enter the value: "))
ans = factorial(number)
print(f"The factorial of {number} is {ans}.")
