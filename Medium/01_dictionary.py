
# Syntax

student = {
    "name": "Vansh",
    "age": 21,
    "course": "MCA"
}

# 1. Accessing Dictionary Values

print(student["name"])       # Vansh
print(student.get("age"))    # 21
print(student.get("grade", "Not Found"))  # Default if key missing

# 2. Adding & Updating Items

student["email"] = "vansh@example.com"  # add new key-value
student["age"] = 22                     # update value
print(student)

# 3. Removing Items

student.pop("course")    # remove by key
student.popitem()        # remove last inserted key-value pair
del student["age"]       # delete specific key
student.clear()          # remove all items
