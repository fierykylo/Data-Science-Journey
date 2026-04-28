#list out of index error
try:
    lst = [10, 20, 30]
    index = int(input("Enter the index: "))
    print(f"Value at index is {lst[index]}")
except IndexError:
    print("Index out of range")
except ValueError:
    print("Please enter a valid value")
