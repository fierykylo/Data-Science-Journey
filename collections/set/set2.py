a = {1,2,3}
b = {3,4,5}
#union
c = (a | b) # same as a.union(b)
print(c)

print (a & b)
print(a - b)
print(a ^ b)
#print(a[0]) wont work as set object is not subscriptable 
