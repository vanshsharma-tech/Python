#Q8. Count how many digits are in a number using a loop.

digit = input("Enter the degit: ")
count = 0
for i in digit:
  if i.isdigit():
    count += 1

print(count)