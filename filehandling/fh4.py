#storing the contents of a file in  list
file_content = []

with open("aarush.txt", "r") as file:

    for line in file:
        file_content.append(line.strip())

print(file_content)