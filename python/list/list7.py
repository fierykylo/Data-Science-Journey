words = ["apple", "bat", "banana", "cat", "elephant"]
n = int(input("Enter the recquired length"))

result = []

for x in words:
    if len(x) > n:
        result.append(x)

print(result)