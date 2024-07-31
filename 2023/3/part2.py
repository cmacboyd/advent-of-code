with open("./3/input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

import re
from math import prod
digits_re = re.compile(r'\d+')
symbols_re = re.compile(r'([^\d\.])')

# collect numbers and symbols
numbers = []
symbols = []
for index, line in enumerate(lines):
	numbers.extend([(index, n.span(), n.group()) for n in re.finditer(digits_re, line)])
	symbols.extend([(index, s.span(), s.group()) for s in re.finditer(symbols_re, line)])

# search functions
def search_horizontal(row, pos):
	horizontal_rows = [(cols, number) for r, cols, number in numbers if r==row]
	# print('horizontal', horizontal_rows)
	# print('h set', set([number for cols, number in horizontal_rows if pos+1 in range(*cols) or pos-1 in range(*cols)]))
	return set([number for cols, number in horizontal_rows if pos+1 in range(*cols) or pos-1 in range(*cols)])

def search_vertical(row, pos):
	vertical_rows = [(cols, number) for r, cols, number in numbers if r==row+1 or r==row-1]
	return set([number for cols, number in vertical_rows if pos in range(*cols)])

def search_diagonal(row, pos):
	diagonal_rows = [(cols, number) for r, cols, number in numbers if r==row+1 or r==row-1]
	return set([number for cols, number in diagonal_rows if pos+1 in range(*cols) or pos-1 in range(*cols)])

def search_adjacent(row, pos):
	adj_num = set()
	# I am assuming there are no duplicate part numbers around each symbol
	adj_num = adj_num.union(search_horizontal(row, pos))
	adj_num = adj_num.union(search_vertical(row, pos))
	adj_num = adj_num.union(search_diagonal(row, pos))
	return adj_num


# go through symbols and search for numbers
rolling_sum = 0
for row, loc, symbol in symbols:
	if symbol == '*':
		pos, _ = loc
		valid_numbers = set()
		valid_numbers = valid_numbers.union(search_adjacent(row, pos))
		if len(valid_numbers) == 2:
			product = prod([int(n) for n in valid_numbers])
			rolling_sum += product

print(rolling_sum)