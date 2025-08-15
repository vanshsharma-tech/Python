person = {"name": "Alice", "age": 25, "city": "Delhi"}

print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 25, 'Delhi'])
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Delhi')])

for key, value in person.items():
    print(key, ":", value)

# copy
new_person = person.copy()

# Nested Dictionary

students = {
    "101": {"name": "Vansh", "marks": 90},
    "102": {"name": "Kashish", "marks": 95}
}

print(students["101"]["name"])   # Vansh

# Dictionary Comprehension

squares = {x: x*x for x in range(1, 6)}
print(squares)   # {1:1, 2:4, 3:9, 4:16, 5:25}
