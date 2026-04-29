n = 4
for i in range(1,5):
    print(" " * (n - i), end="")
    for j in range(1,i+1):
        print(j, end=" ")
    for k in range(1,i):
        print(k, end = " ")
    print()