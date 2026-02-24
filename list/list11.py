lst = [10, 23, 4, 5, 6,5 ,6 ,3 ,1 ,23, 102 , 12, 34, 123, 4545 ,67, 87, 78, 778, 787, 902, 101]
highest = float('-inf')
secondhighest = float('-inf')

for x in lst:
    if x > highest:
        secondhighest = highest
        highest = x
    elif x > secondhighest and x != highest:
        secondhighest = x

print(secondhighest)