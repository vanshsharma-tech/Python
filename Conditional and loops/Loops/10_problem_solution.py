# Q10. Check if a given number is a prime number (using loops).

number = int (input('Enter the number to check: '))
is_prime = True
for i in range(2,number):
  if number % i == 0:
    is_prime = False

if is_prime:
  print(f"{number} is a prime number")
else:
  print(f"{number} is not a prime number")