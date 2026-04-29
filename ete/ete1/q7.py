lines = []

print("Enter the lines")

while(True):
    line = input("")
    if (line == ""):
        break
    lines.append(line)

lines = [line.upper() for line in lines]

print(lines)