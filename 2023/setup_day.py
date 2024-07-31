import webbrowser
from datetime import datetime
from pathlib import Path
from getpass import getuser

# Get the day number we are dealing with automatically by counting from the 30th of november
# start_date = datetime(2022,11,30)
# this_day = (datetime.now() - start_date).days
this_day = 7
print(f"Running setup script for day {this_day} of advent of code")

# Open today's problem in a browser
url = f"https://adventofcode.com/2023/day/{this_day}"
webbrowser.get().open(url)

# Make a directory with today's name, and the files we want
Path(f"/Users/{getuser()}/Projects/advent-of-code/2023/{this_day}").mkdir(exist_ok=True)

code_stub = f"""with open("./{this_day}/test_input.txt", "r") as f:\n\tlines = f.readlines()\n\n"""
for part in [1, 2]:
    this_file = Path(f"/Users/{getuser()}/Projects/advent-of-code/2023/{this_day}/part{part}.py")
    this_file.touch(exist_ok=True)
    this_file.write_text(code_stub)

Path(f"/Users/{getuser()}/Projects/advent-of-code/2023/{this_day}/part2.py").touch(exist_ok=True)
Path(f"/Users/{getuser()}/Projects/advent-of-code/2023/{this_day}/input.txt").touch(exist_ok=True)
Path(f"/Users/{getuser()}/Projects/advent-of-code/2023/{this_day}/test_input.txt").touch(exist_ok=True)

# TODO: this request gives me back a 400 error, probably something to do with authentication
# TODO: you can pip install aocd to work with the site properly
# Get today's input file and save it to the directory we made
# req = requests.get(f"{url}/input")
# print(req)