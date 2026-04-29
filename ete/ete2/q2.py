text = input("Enter a string : ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for key, value in freq.items():
    print(f"{key} => {value}")
    
