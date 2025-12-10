# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter username : ")


if len(username) > 12:
    print("The length of your username can't be more than 12")
elif not username.find(" ") == -1:
    print("There should be no spaces in your username ")
elif not username.isalpha():
    print("The username should only contain alphabets")
else:
    print(f"Welcome, {username}!!")
