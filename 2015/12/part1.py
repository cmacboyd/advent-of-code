import re

with open("./2015/12/input.txt", "r") as f:
    string = f.read()

print(sum([int(i) for i in re.findall(r'-?\d+', string)]))