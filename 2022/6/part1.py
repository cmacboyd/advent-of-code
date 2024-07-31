with open("./6/input.txt", "r") as f:
    buffer = f.read().strip()

window = []
i = 4

while i < len(buffer):
    this_window = buffer[i-4:i]
    if len(set(this_window)) == 4:
        break
    i += 1

print(f"you need to process {i} characters")