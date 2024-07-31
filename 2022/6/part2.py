with open("./6/input.txt", "r") as f:
    buffer = f.read().strip()

window = []
i = 14

while i < len(buffer):
    this_window = buffer[i-14:i]
    if len(set(this_window)) == 14:
        break
    i += 1

print(f"you need to process {i} characters")