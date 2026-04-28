lst = ['Black', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'White']

result = ["Black" if x == "White" else "White" if x == "Black" else x for x in lst]
print(result)