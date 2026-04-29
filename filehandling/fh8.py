#copy contents of one file into another

with open("aarush.txt", "r") as src, open("destination.txt", "w") as dest:
    for line in src:
        dest.write(line)
        