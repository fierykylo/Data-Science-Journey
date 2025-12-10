#hypotenuse of a right angled triangle

import math as m

b = float(input("Enter the base of the triangle : "))
h = float(input("Enter the height of the triangle : "))

perpendicular = m.sqrt(pow(b, 2) + pow(h, 2))
print(f"The hypotenuse is of the triangle is {round(perpendicular, 2)}cm")