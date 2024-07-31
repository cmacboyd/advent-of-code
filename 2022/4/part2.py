with open("./4/input.txt", "r") as f:
    lines = (line.strip().split(",") for line in f.readlines())


def make_number_set(text):
    start, end = [int(num) for num in text.split("-")]
    end += 1
    return set(list(range(start, end)))


def has_overlap(one, two):
    one_set = make_number_set(one)
    two_set = make_number_set(two)
    
    if one_set.isdisjoint(two_set):
        return False
    else:
        return True


overlap_count = len([line for line in lines if has_overlap(*line)])
print(f"The overlap count is {overlap_count}")