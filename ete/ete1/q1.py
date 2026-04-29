#replace every instance of n with e in a python programme

text = input("Enter the text : ")
res = ""

for ch in text:
    if (ch == "n"):
        result += "e"
    else:
        result += ch