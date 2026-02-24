lst = [1,1,2,3,4,5,6,6,6,7,7,8,8,9,9,9,9,9,9,9,9,10]

freq = {}

for x in lst:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

for key, value in freq.items():
    print(f"{key} occurs {value} times")
