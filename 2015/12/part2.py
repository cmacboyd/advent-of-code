import re

with open("./2015/12/input.txt", "r") as f:
    string = f.read()

# need to do a buffer stack and read from { to }, then pop off
brace_stack = []
exclude = []

for index, char in enumerate(string):
    if char == '{':
        brace_stack.append(index)
    
    elif char == '}':
        start = brace_stack.pop()

        if 'red' in eval(string[start:index+1]).values():
            exclude.append(range(start, index+1))

s = 0
for match in re.finditer(r'-?\d+', string):
    start = match.span()[0] 
    
    if not any([start in r for r in exclude]):
        s += int(match.group())


print(s)


# print(re.sub(r'\{.*"red".*\}', '', string))