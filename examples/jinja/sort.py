# Open the file in read mode and read lines
with open("paramaters.txt", "r") as file:
    lines = file.readlines()

# Remove duplicates and sort
lines = sorted(list(set(lines)))

# Open the file in write mode and write sorted lines
with open("paramaters.txt", "w") as file:
    for line in lines:
        file.write(line)
