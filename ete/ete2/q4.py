def countdown(n):
    if n < 0:
        print(".....")
        return
    print(n, end = " ")
    countdown(n - 1)

countdown(5)