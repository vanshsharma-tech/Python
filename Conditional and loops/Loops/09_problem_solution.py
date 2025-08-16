# Q9. Print the Fibonacci series up to n terms.
num = 0
prev = 0
next =1
for i in range(1, 11):
    val = prev + next
    prev = next
    next = val
    print(val,end=' ')

