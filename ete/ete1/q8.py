try:
    # Step 1: Append input to file
    with open("notes.txt", "a") as file:
        for i in range(1, 4):
            line = input(f"Enter line {i}: ")
            file.write(line + "\n")

    # Step 2: Read and display with line numbers
    print("\nContents of notes.txt:")

    with open("notes.txt", "r") as file:
        count = 1
        for line in file:
            print(f"{count}. {line.strip()}")
            count += 1

except IOError:
    print("Error occurred while accessing the file!")