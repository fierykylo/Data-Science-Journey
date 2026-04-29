with open("aarush.txt", "a") as file:
    
    text = input("Enter the text that you wish to append : ")
    file.write("\n" + text)

with open("aarush.txt", "r") as file:
    content = file.read()
    print(content)
