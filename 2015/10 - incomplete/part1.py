def look_say(string):
    new_string = ""

    i = 0
    current_number = string[0]
    counter = 0
    while i < len(string):
        if string[i] == current_number:
            counter += 1
        else:
            new_string += f"{counter}{current_number}"
            current_number = string[i]

        i += 1
        if i == len(string):
            new_string += f"{counter}{current_number}"

    return new_string

starter = "3113322113"
for i in range(1,41):
    starter = look_say(starter)
    print(i, len(starter))