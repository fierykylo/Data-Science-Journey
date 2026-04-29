lst = [1,2,3,4,5,6]

try:
    index = int(input("Enter the target index : "))
    print(f"Value : {lst[index]}")
except IndexError:
    print("Index out of bounds please enter a valid index")
    