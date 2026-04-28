#checking for substring using memebership operator 

ogstring = input("Enter a string : ")
substring = input("Enter the substring : ")

if substring in ogstring:
    print("Present")
else:
    print("Not present")