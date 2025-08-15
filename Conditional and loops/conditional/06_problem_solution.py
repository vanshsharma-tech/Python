#Q6. Take three numbers and find the largest among them.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print("The first number 1 is largest")
elif num2 > num1 and num2 > num3:
    print("The second number 2 is largest")
elif num3 > num1 and num3 > num2:
    print("The third number 3 is largest")
else:
    print("All numbers is equal")
