# Tuple Methods

letters = ("a", "b", "c", "a")

print(len(letters))  # 4
print(letters.count("a"))  # 2
print(letters.index("b"))  # 1

# Tuple Packing & Unpacking
# Packing
person = ("Vansh", 21, "MCA")

# Unpacking
name, age, course = person
print(name)   # Vansh
print(age)    # 21

# Nested Tuples
nested = (("apple", "banana"), (1, 2, 3))
print(nested[0][1])  # banana
