#check similar elements in a list
lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]

common = list(set(lst1) & set(lst2))
print(common)