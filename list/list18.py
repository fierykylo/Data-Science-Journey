List1 = [1,3,2,1,2,1,4,5,1,3,2,5] 

freq = {}

for num in List1:
    freq[num] = freq.get(num, 0) + 1

maxnum = max(freq, key=freq.get)

result = []
for num in List1:
    if num != maxnum:
        result.append(num)

print(result)