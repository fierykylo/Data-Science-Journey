with open("geek.txt", "w") as file:
    file.write("Hello, python\n")
    file.write("File handling is easy with python")

with open("geek.txt", "r") as file:
    content = file.read()
    print(content)