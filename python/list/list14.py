list =  [0,1,2,3,4,5]
n = len(list)
for i in range(0,n - 1,2):
        temp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = temp
    
print(list)