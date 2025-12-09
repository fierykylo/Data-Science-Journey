#excercise 2 
# just telling the price of an item that you have bought super simple super easy

item = input("Item purchased : ")
price = int(input("Price of item purchased : "))
quantity = int(input("Quantity of the item purchased : "))

total = price * quantity
print(f"you bought {quantity} {item}")
print(f"Total price is : Rs.{total}")