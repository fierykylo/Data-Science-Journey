with open("aarush.txt", "r") as file:
    words = file.read().split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

print(longest)