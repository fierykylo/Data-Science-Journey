library = {
    "Aarush": {"Python": 10, "Math": 5},
    "Rahul": {"Science": 8, "English": 12}
}

for member, books in library.items():
    total_fine = 0
    for book, days in books.items():
        if(days > 7):
            total_fine += (days - 7) * 2
    print(f"{member} has to pay {total_fine}")