#min max occurence of a string

s = input("Enter a string : ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

maxChar= max(freq, key=freq.get)
minChar= min(freq, key=freq.get)

print(maxChar)
print(minChar)