import re
from itertools import cycle

with open('./2015/7/input2.txt') as f:
    lines = [line.strip() for line in f.readlines()]

test = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
""".strip()

test = [t.strip() for t in test.split('\n')]

single_operation = r'([a-z]+|NOT [a-z]+|\d+) -> ([a-z]+)'
double_operation = r'([a-z]+|\d+) (AND|OR|RSHIFT|LSHIFT) ([a-z]+|\d+) -> ([a-z]+)'

circuit = {}
processed = set()
icycle = cycle(range(len(lines)))
i = next(icycle)
while len(processed) < len(lines):
    
    if i not in processed:
        if (match:=re.match(single_operation, lines[i])):
            a, b = match.groups()

            if a.isdigit():
                a = int(a)

            if not (type(a) is int):
                if a not in circuit and not a.startswith('NOT'):
                    pass 
                
                elif a.startswith('NOT') and a.replace('NOT ', '') not in circuit:
                    # we need to process this one later, pass 
                    pass
                else:
                    # we should be able to process this one
                    if not type(a) is int and a.startswith('NOT'):
                        a = a.replace('NOT ', '')
                        circuit[b] = ~circuit[a] + 2**16
                    elif not type(a) is int and a.isalpha():
                        circuit[b] = circuit[a]

                    # we processed the instruction, remove this
                    processed.add(i)
            else:
                circuit[b] = int(a)

                # we processed the instruction, remove this
                processed.add(i)

        elif (match:=re.match(double_operation, lines[i])):
            a, op, b, c = match.groups()

            # get a and b into their proper forms
            if a.isdigit():
                a = int(a)
            if b.isdigit():
                b = int(b)

            # see if we need to wait to actually send the signal
            if (not type(a) is int and a not in circuit) or (not type(b) is int and b not in circuit):
                # need to process this later, pass
                pass
            else:
                if op == 'AND':
                    circuit[c] = circuit.get(a, a) & circuit.get(b, b)
                elif op == 'OR':
                    circuit[c] = circuit.get(a, a) | circuit.get(b, b)
                elif op == 'RSHIFT':
                    circuit[c] = circuit.get(a, a) >> circuit.get(b, b)
                elif op == 'LSHIFT':
                    circuit[c] = circuit.get(a, a) << circuit.get(b, b)
                else:
                    print('eeek operation')

                processed.add(i)

    i = next(icycle)
    # print(len(processed), circuit)
    # print([line for i, line in enumerate(lines) if i not in processed])
    # if len(processed) == 9:
    #     break


print(circuit)