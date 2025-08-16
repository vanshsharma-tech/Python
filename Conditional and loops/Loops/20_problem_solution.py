
#Q20. Write a program that check a number perfect number or not  
number = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i

if sum_of_divisors == number:
    print(f"{number} is a perfect number✅")
else:
    print(f"{number} is a perfect number❌")
