def countLists(lst):
    count = 0
    for x in lst:
        if isinstance(x, list):
            count += 1
            count += countLists(x) # list within lists
    return count

lst = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
result = countLists(lst)
print(result)