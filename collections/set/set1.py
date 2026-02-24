a = {1,2}
a.add(3) # can only add one element
print(a)
a.update([4,5]) # can update multiple elements
print(a)

#removal
a.pop() #random
a.remove(2) # if 2 doesnt exist error occurs
print(a)
a.discard(10) # safe removal
a.clear() # khel khatam sab khali
print(a) #set() gets printed 