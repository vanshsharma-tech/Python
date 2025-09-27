arr = [5, 2, 9, 1, 5, 6]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap using temp variable
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr[n-2])
