text = "JAVA"
remove_char = "A"
result = ""

for i in text:
    if (i != remove_char):
        result += i

print(result)