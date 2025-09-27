#
def fibonachi(num, a=0, b=1, count=0):
    if count == num:
        return
    print(a, end=" ")
    fibonachi(num, b, a + b, count + 1)


fibonachi(10)
