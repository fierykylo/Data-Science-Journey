text = input("Enter text : ")
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

max_freq = max(freq, key = freq.get)
min_freq = min(freq, key = freq.get)

print(freq[max_freq])
print(freq[min_freq])

