lst = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Enter the number that you want in the list : "))

if (num in lst):
    print("found")

for i in lst:
    if(i == num):
        print(f"found at index {i}")