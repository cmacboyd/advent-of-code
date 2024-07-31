# We want to find the top three elves with the most calories in their snacks

# get the data from file
with open("./1/input.txt", "r") as f:
    snacks = (line.strip() for line in f.readlines())


elves = []
this_elf = 0
for snack in snacks:
    if snack == "":
        elves.append(this_elf)
        this_elf = 0
        continue

    this_elf += int(snack)

top_three = sorted(elves, reverse=True)[:3]

print(f"The best elves have {sum(top_three)} calories")