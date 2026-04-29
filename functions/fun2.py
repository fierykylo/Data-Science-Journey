#iterative
def fibonacci_iter(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Example
n = int(input("Enter n: "))
fibonacci_iter(n)

