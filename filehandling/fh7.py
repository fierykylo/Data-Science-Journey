with open("aarush.txt", "r") as file:
    content = file.read().lower()

    words = content.split()

    freq = {}

    for word in words:
        if(word in freq):
            freq += 1
        else:
            freq[word] = 1
