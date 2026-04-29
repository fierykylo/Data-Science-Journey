students = [
    ("Aarush", 85, 90, 88),
    ("Rahul", 75, 80, 70),
    ("Neha", 92, 95, 94)
]

highest_avg = 0
topper = ""

print("Average Marks:")

for student in students:
    name, m1, m2, m3 = student
    avg = (m1 + m2 + m3) / 3
    print(name, ":", avg)

    if avg > highest_avg:
        highest_avg = avg
        topper = name

print("\nTopper:", topper)

print("\nStudents scoring >80 in all subjects:")
for student in students:
    name, m1, m2, m3 = student
    if m1 > 80 and m2 > 80 and m3 > 80:
        print(name)