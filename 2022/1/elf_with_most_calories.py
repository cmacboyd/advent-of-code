# We want to find the elf with the most calories in their snacks

# get the data from file
with open("./1/input.txt", "r") as f:
    snacks = (line.strip() for line in f.readlines())

most_calories = 0
this_elf = 0 
best_elf = 0
for snack in snacks:
    if snack == "":
        this_elf = 0
        continue

    this_elf += int(snack)
    best_elf = max(this_elf, best_elf)

print(f"The best elf has {best_elf} calories")