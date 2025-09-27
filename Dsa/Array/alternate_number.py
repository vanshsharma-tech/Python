lst = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, len(lst) - 1, 2):
    temp = lst[i]
    lst[i] = lst[i + 1]
    lst[i + 1] = temp

print(lst)
