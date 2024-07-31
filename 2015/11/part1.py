from string import ascii_lowercase

to_number = {l: i for i, l in enumerate(ascii_lowercase)}
to_letter = {i: l for i, l in enumerate(ascii_lowercase)}

start = 0
straights = set()
window = ascii_lowercase[start:start+3]
while len(window) == 3:
    straights.add(window)
    start += 1
    window = ascii_lowercase[start:start+3]

def check1(pw: str) -> bool:
    # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. 
    # They cannot skip letters; abd doesn't count.
    start = 0
    window = pw[start: start+3]
    while len(window) == 3:
        if window in straights:
            return True
        start += 1
        window = pw[start: start+3]
    return False

def check2(pw: str) -> bool:
    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    return True

def check3(pw: str) -> bool:
    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

    start = 0
    window = pw[start:start+2]

    double_letters = set()
    double_indices = set()

    while len(window) == 2:
        if window[0] == window[1] and \
            window[0] not in double_letters and \
                start not in double_indices and start+1 not in double_indices:
            double_letters.add(window[0])
            double_indices.add(start)
            double_indices.add(start+1)

            if len(double_letters) == 2:
                return True

        start += 1
        window = pw[start:start+2]

    return False


def checks(pw: str) -> bool:
    if check1(pw) and check2(pw) and check3(pw):
        return True
    return False


# check tests 
assert check1('hijklmmn') and not check2('hijklmmn')
assert check3('abbceffg') and not check1('abbceffg')
assert not check3('abbcegjk')


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def increment_password(pw: str) -> str:
    # go str -> base26, increment, base26 -> str
    next_numeric = sum([(to_number[letter]*(26**power)) for power, letter in enumerate(pw[::-1])])+1
    next_pw =  ''.join([to_letter[num] for num in numberToBase(next_numeric, 26)])
    if len(next_pw) < 8:
        next_pw = 'a'*(len(pw)-len(next_pw)) + next_pw
    
    # print(next_pw)
    return next_pw


def next_valid_password(password: str) -> str:
    password = increment_password(password)

    while not checks(password):
        password = increment_password(password)

    return password


# assert next_valid_password('abcdefgh') == 'abcdffaa'
# assert next_valid_password('ghijklmn') == 'ghjaabcc'

# part 1 question
# print(next_valid_password('cqjxjnds'))

# part 2 question
print(next_valid_password('cqjxxyzz'))
