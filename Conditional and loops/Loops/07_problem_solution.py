# Q7. Take a number n and print its factorial using a loop

number = int(input("Enter a number: "))
fact = 1
for i in range(1, number + 1):
    fact *= i
print(f"Factorial of {number}: {fact}")
