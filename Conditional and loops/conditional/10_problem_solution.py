#Q10. Build a program for a simple calculator.

# Simple Calculator Program

print("----- Simple Calculator -----")
print("Operations: +  -  *  /")

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator! Please choose +, -, * or /.")
