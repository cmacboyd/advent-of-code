import re

with open("./2015/8/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

code_length = sum([len(s) for s in lines])
string_pattern = r"\\x[a-f0-9]{2}|\\.|."
string_length = sum([len(re.findall(string_pattern, s[1:-1])) for s in lines])

print(code_length, string_length, code_length - string_length)
