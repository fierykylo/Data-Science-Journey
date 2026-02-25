n = 9
for i in range(n):
    for k in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(j+1, end = "")
    for x in range(n - 1 - i,0,-1):
        print(x, end="")
    
    print("")
    
