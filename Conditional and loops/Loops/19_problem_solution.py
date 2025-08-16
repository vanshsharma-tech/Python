# Print all prime numbers between 1 and 100.


def prime_numbers(val):
    is_prime = True
    if val < 2:
        is_prime = False
    for i in range(2, val):
        if val % i == 0:
            is_prime = False

    if is_prime:
        return val


for i in range(1, 101):
    if prime_numbers(i):
        print(prime_numbers(i), end=" ")
