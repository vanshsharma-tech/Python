# def decimal_to_binary(num):
#     ans = []
#     while num != 0:
#         rem = num % 2
#         ans.append(rem)
#         num //= 2

#     return ''.join(str(x) for x in ans[::-1])


# val = decimal_to_binary(8)
# # val.reverse()
# print(val)


def decimal_to_binary(num):
    ans = 0
    place = 1  # keeps track of position (units, tens, hundreds...)

    while num != 0:
        rem = num % 2
        ans = rem * place + ans  # put remainder in correct place
        num //= 2
        place *= 10  # shift place value (like decimal to binary digits)

    return ans


# Example
print(decimal_to_binary(8))  # 1000
print(decimal_to_binary(13))  # 1101
