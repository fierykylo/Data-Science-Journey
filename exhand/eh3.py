try:
    with open("Aarush.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found !!!")