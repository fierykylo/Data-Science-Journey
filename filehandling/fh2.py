#reading n lines at a time

n = int(input("Enter the number of lines you want to read : "))
with open("aarush.txt", "r") as file:

    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end = " ")