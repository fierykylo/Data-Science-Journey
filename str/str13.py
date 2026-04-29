# Sample data
text = "Python is fun"
words = ["Python", "is", "fun"]

# 1. replace()
print("1. replace():")
replaced = text.replace("fun", "awesome")
print(replaced)


# 2. endswith()
print("\n2. endswith():")
print(text.endswith("fun"))


# 3. join()
print("\n3. join():")
joined = " ".join(words)
print(joined)


# 4. format()
print("\n4. format():")
name = "Aarush"
age = 20

formatted = "My name is {} and I am {} years old".format(name, age)
print(formatted)