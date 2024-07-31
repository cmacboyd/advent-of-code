from string import ascii_lowercase
from itertools import product
import re

with open("./2015/5/input.txt", "r") as f:
	strings = f.readlines()

combinations = [''.join(e) for e in product(ascii_lowercase, ascii_lowercase)]
pattern = r'([a-z]).\1'

def is_nice(string):
    if not any([string.count(c) >= 2 for c in combinations]):
        return False

    if not re.search(pattern, string):
        return False

    return True


test = [
    'qjhvhtzxzqqjkmpb',
    'xxyxx',
    'uurcxstgmygtbstg',
    'ieodomkazucvgmuy'
]

nice_count = 0
for string in strings:
    if is_nice(string):
        nice_count += 1

print(nice_count)