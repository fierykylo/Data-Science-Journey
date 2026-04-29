n = 4

for i in range(1, n + 1):
    # spaces
    print(" " * (n - i), end="")

    # decreasing part
    for j in range(i, 0, -1):
        print(j, end=" ")

    # increasing part
    for j in range(2, i + 1):
        print(j, end=" ")

    print()