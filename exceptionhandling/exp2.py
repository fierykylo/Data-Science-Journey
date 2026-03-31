try:
    user_input = input("Enter a number : ")
    if not user_input.isdigit():
        raise ValueError("Not a valid integer")
    num = int(user_input)
    print(f"you entered {num}")
except ValueError as e:
    print("Error:", e)