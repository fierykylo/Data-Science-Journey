text = input("enter : ")
first_char = text[0]
result = first_char

for ch in text:
    if (ch == first_char):
        result += "#"
    else:
        result += ch