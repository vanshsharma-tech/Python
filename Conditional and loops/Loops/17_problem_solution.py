# Q17. Reverse a number using a loop (e.g., 123 → 321).

# Method 1 ->

number = 123
rem = None
ans = 0

while number > 0:
    rem = number % 10
    ans = ans * 10 + rem
    number //= 10

# print(ans)


# Method 2 ->

number = "123"
ans = ""

for i in number:
    ans = i + ans

# print(int(ans))
# print(ans)
