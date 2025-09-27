# Q6. ⚖️ Check whether a number is even or odd without using % operator.

# Quick Explanation:-
# num & 1 checks the least significant bit
# If it's 0, the number is even; if it's 1, the number is odd.
# 7 & 1 = 1 (odd)
# 0111 & 0001 = 0001
# 8 & 1 = 0 (even)
# 1000 & 0001 = 0000

num = int(input("Enter a number: "))
if num & 1 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
