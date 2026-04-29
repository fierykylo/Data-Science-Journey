#reading an entire file

with open("aarush.txt", "r") as file:
    content = file.read()
    print(content)
