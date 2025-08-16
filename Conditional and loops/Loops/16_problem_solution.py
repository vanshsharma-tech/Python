# Q16. Find the sum of digits of a number (e.g., 123 → 1+2+3=6).

# Method 1 ->

digit = "123"
val = 0
for i in digit:
    val += int(i)

print(val)

# Method 2 ->

digit = 123

add = 0

while digit > 0:
    rem = digit % 10
    add += rem
    digit //= 10

print(add)
