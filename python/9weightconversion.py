#simple code to perform weight conversion 

weight = float(input("Enter your weight please : "))
unit = input("What is the unit of your weight (enter kg or lbs) ? ").lower()

if unit == "kg":
    weight *= 2.205
    unit = "lbs."
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "lbs":
    weight /= 2.205
    unit = "kg."
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not a vaild unit")