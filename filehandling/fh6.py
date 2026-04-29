with open("data.txt", "r") as file:
    content = file.read()

# Count characters
char_count = len(content)

# Count words
word_count = len(content.split())

# Count lines
line_count = content.count('\n') + 1

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)