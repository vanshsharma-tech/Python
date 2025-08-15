# str = "Vansh Sharma"
# print(str)

# Methods of string

# 1. Basic String Operations

str1 = "Vansh"
name = "Python"
print(len(name))  # length → 6
print(name[0])  # indexing → 'P'
print(name[-1])  # negative indexing → 'n'
print(name[0:4])  # slicing → 'Pyth'
print(name.upper())  # 'PYTHON'
print(name.lower())  # 'python'
print(name.replace("Py", "My"))  # 'Mython'


# 2. String Methods (Most Used)

s = "   hello world   "

print(s.strip())       # remove spaces → 'hello world'
print(s.lstrip())      # remove left spaces
print(s.rstrip())      # remove right spaces

print(s.split())       # split into list → ['hello', 'world']
print("-".join(["a","b","c"]))  # join → 'a-b-c'

print("apple".startswith("a"))  # True
print("apple".endswith("e"))    # True

print("Hello".find("l"))   # index of first 'l' → 2
print("Hello".count("l"))  # count → 2

# 3. String Formatting

name = "Vansh"
age = 21

# f-string (best way)
print(f"My name is {name} and I am {age} years old.")

# format method
print("My name is {} and I am {} years old.".format(name, age))

# % formatting
print("My name is %s and I am %d years old." % (name, age))

# 4. Escape Characters

print("Hello\nWorld")   # newline
print("Hello\tWorld")   # tab
print("He said \"Python is easy\"")  # quotes

# 5. String Checking Methods

s = "Python123"

print(s.isalpha())   # False (contains numbers)
print(s.isdigit())   # False
print(s.isalnum())   # True (letters + numbers)
print(s.islower())   # False
print(s.isupper())   # False
print(s.isspace())   # False

