a = {1,2,3}
b = {3,4,5}
#union
c = (a | b) # same as a.union(b)
print(c)

print (a & b) #3
print(a - b) # 1 2
print(a ^ b) # 1 2 4 5
#print(a[0]) wont work as set object is not subscriptable 
