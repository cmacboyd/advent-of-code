with open("./4/input.txt", "r") as f:
    lines = (line.strip().split(",") for line in f.readlines())


def make_number_set(text):
    start, end = [int(num) for num in text.split("-")]
    end += 1
    return set(list(range(start, end)))


def contains_each_other(one, two):
    one_set = make_number_set(one)
    two_set = make_number_set(two)
    
    if one_set.issubset(two_set) or two_set.issubset(one_set):
        return True
    else:
        return False


containing_count = len([line for line in lines if contains_each_other(*line)])
print(f"The containing count is {containing_count}")