# **** # 1,4
# ***  # 2,3
# **   # 3,2
# *    # 4,1

for i in range(4):
    for j in range(4, i, -1):
        print("*", end=" ")
    print()
