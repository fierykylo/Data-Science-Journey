lst = ["abc", "aba", "xyz", "pqr", "zzz"]
count = 0
for word in lst:
    if (len(word) >= 2 and word[0] == word[-1]):
        count += 1

print(count)