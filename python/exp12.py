numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    index = int(input("Enter an index : "))
    print(numbers[index])
except ValueError:
    print("Please enter a valid value")
except IndexError:
    print("Please enter a valid index")