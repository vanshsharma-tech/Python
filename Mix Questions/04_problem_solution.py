# Find the square root of a number without using ** or math.sqrt()
num = int(input("Enter the number: "))


# def sqrt_num(num):
#     return pow(num,0.5)
def sqrt_num(num):
    ans = 0
    i = 1
    while i * i < num:
        i += 1
        ans = i
    return ans

print(f"Square root of {num} is approximately {sqrt_num(num)}")
# print(f"The Square root of {num} is {sqrt_num(num)}.")
