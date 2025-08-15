# List Methods 

nums = [1, 2, 3]

nums.append(4)          # add at end → [1,2,3,4]
nums.insert(1, 10)      # insert at index 1 → [1,10,2,3,4]
nums.extend([5, 6])     # extend list → [1,10,2,3,4,5,6]

nums.remove(10)         # remove value 10
nums.pop()              # remove last element
nums.pop(1)             # remove element at index 1

nums.sort()             # sort ascending
nums.sort(reverse=True) # sort descending

nums.reverse()          # reverse list
print(nums.index(3))    # index of element 3
print(nums.count(2))    # count occurrences of 2


# Useful Built-in Functions

numbers = [5, 10, 15, 20]

print(len(numbers))   # length → 4
print(min(numbers))   # minimum → 5
print(max(numbers))   # maximum → 20
print(sum(numbers))   # sum → 50
