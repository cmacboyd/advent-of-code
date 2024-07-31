with open("./1/input.txt", "r") as f:
	lines = f.readlines()

def get_first_digit(line):
	for letter in line.strip():
		if letter.isdigit():
			return letter
	
	print(f"no letter in this line: {line}")


numbers = []
for line in lines:
	first_digit = get_first_digit(line)
	last_digit = get_first_digit(line[::-1])
	numbers.append(int(first_digit+last_digit))

print(sum(numbers))