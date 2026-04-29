lst = [1,2,3,4,5,6,7,8,9,10]

if (len(lst) != len(set(lst))):
    print("Duplicates found !!")
else:
    print("No duplicates !!")