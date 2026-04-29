text = input("Enter a string : ")
target = input("Enter the string you need to find : ")

print(text.find(target)) #gives - 1
print(text.index(target)) #gives error if not found
