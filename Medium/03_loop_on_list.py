
# Looping Through Lists

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# with index
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# List Comprehension (Shortcut)

squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

even = [x for x in range(10) if x % 2 == 0]
print(even)      # [0, 2, 4, 6, 8]

# ⚡ Key Points

# Lists are mutable → you can change elements.

# You can use them for arrays, stacks, queues, or matrices.

# Extremely powerful when combined with loops & comprehensions.