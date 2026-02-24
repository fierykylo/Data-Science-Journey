#join

greeting = ["Hello", "World"]
sentence = ", ".join(greeting)
print(sentence)

#endswith

love = "love"
print(love.endswith("ly")) #gives False as it doesnt end with ly

#replace 

s = "I love Javascript"
s.replace("JavaScript", "Python")

print(s)

#format

name = "Aarush Dubey"
print("Name : {}".format(name))
