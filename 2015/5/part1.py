from string import ascii_lowercase

with open("./2015/5/input.txt", "r") as f:
	strings = f.readlines()


def is_nice(string):
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        return False

    vowels = 'aeiou'

    vowel_count = sum([string.count(v) for v in vowels if v in string])

    if vowel_count < 3:
        return False

    if not any([l*2 in string for l in ascii_lowercase]):
        return False

    return True


test = [
    'ugknbfddgicrmopn',
    'aaa',
    'jchzalrnumimnmhp',
    'haegwjzuvuyypxyu',
    'dvszwmarrgswjxmb'
]

nice_count = 0
for string in strings:
    if is_nice(string):
        nice_count += 1

print(nice_count)