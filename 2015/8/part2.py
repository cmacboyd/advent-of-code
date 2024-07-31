import re

with open("./2015/8/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

code_length = sum([len(s) for s in lines])


pattern1 = r"\\x[a-f0-9]{2}"
pattern2 = r"\\x(?![a-f0-9]{2})|\\[^x]"

encode_length = 0
for line in lines:
    # add one backslash for each of these patterns present
    if re.findall(pattern1, line):
        encode_length += len(re.findall(pattern1, line))

    # add two backslashes for each of these patterns present
    if re.findall(pattern2, line):
        encode_length += 2*len(re.findall(pattern2, line))

    encode_length += len(line)+4

print(code_length, encode_length,  encode_length - code_length)
# 2088 was too high
# 2085 right answer - had wrong regex for hex
# 1408 was too low