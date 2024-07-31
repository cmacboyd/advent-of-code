import re

with open("./1/input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

word_to_digit = {
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
}

digit_starts = ''.join([w[0] for w in word_to_digit.keys()])
digit_ends = ''.join([w[-1] for w in word_to_digit.keys()])

def get_written_digit(line, pos, reverse=False):
	l = line[pos:]

	if not reverse and (match:=re.match(f'({"|".join([w for w in word_to_digit.keys()])})', l)):
		return str(word_to_digit.get(match.group()))
	elif reverse and (match:=re.match(f'({"|".join([w[::-1] for w in word_to_digit.keys()])})', l)):
		return str(word_to_digit.get(match.group()[::-1]))
	else:
		return False
	

def get_first_digit(line, reverse=False):
	for pos, letter in enumerate(line.strip()):
		if letter.isdigit():
			return letter
		elif not reverse and letter in digit_starts:
			if digit:=get_written_digit(line, pos):
				return digit
		elif reverse and letter in digit_ends:
			if digit:=get_written_digit(line, pos, reverse=True):
				return digit

numbers = []
for line in lines:
	first_digit = get_first_digit(line)
	last_digit = get_first_digit(line[::-1], reverse=True)
	numbers.append(int(first_digit+last_digit))

print(sum(numbers))