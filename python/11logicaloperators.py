# Movie Ticket Eligibility Checker

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()
is_weekend = input("Is it the weekend? (yes/no): ").lower()
is_banned = False  # for fun, imagine a person banned for talking loudly in movies

# Convert to boolean
is_student = (is_student == "yes")
is_weekend = (is_weekend == "yes")

# 1️⃣ using AND - must satisfy both
if age >= 18 and not is_banned:
    print("You can buy an adult ticket.")

# 2️⃣ using OR - either condition works
if age < 18 or is_student:
    print("You get a discount!")

# 3️⃣ using NOT - negating a condition
if not is_weekend:
    print("Weekday pricing applies.")

# 4️⃣ combining all three
if (age >= 18 and is_student) or (is_weekend and not is_banned):
    print("Special offer unlocked! 🎉")
