# Q10. 🔁 Print the first 10 natural numbers without using a loop (use recursion).


# def addition_of_natural_numbers(num):
#     if num == 0:
#         return 0

#     return num + addition(num - 1)


# ans = addition_of_natural_numbers(10)
# print(ans)

def print_natural_numbers(num):
  if num==0:
    return
  
  print_natural_numbers(num-1)
  print(num)

print_natural_numbers(10)
