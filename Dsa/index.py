def merged(num1, num2):
    new_arr = []
    for i in num1:
        new_arr.append(i)

    for i in num2:
        new_arr.append(i)

    return new_arr


l1 = [1,3]
l2 = [2]


def median(arr):
    count = 0
    for i in arr:
        count += 1

    ind = count / 2
    if count % 2 == 0:
        val = int(count / 2)
        ans = arr[val-1] + arr[val]
        print(ans/2)
        
    else:
        val = int(count / 2)
        ans = arr[val]
        print(ans)


res = merged(l1, l2)
print(res)
# print(median(res))
median(res)


# print(merged(l1, l2))
