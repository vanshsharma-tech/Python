#Q18. Find the GCD of two numbers using a loop.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(48, 18))  
