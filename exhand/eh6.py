try:
    a = input("Enter a number : ")
    b = input("Enter a number : ")

    if not (a.isdigit() and b.isdigit()):
        raise TypeError("Value must be numeric")
    
    a = int(a)
    b = int(b)
    sum = a + b
    print(sum)
except TypeError as e:
    print("Error", e)
except ValueError as e:
    print("Value Error")
except:
    print("Error!!")
    
       