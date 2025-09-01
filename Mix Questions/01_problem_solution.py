# 👋 Print "Hello, World!" 100 times without using a loop.


def hellow_world(num):
    if num == 0:
        return
    # print("Hellow World")

    return print("Hellow world!"), hellow_world(num - 1)


hellow_world(100)
