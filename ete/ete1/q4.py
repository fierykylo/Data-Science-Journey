def bunny_ears(n):
    if n == 0:
        return 0
    return 2 + bunny_ears(n - 1)

    

ears = bunny_ears(2)
print(ears)