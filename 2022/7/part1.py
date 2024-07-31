from collections import defaultdict
import re

with open("./7/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
        

files = defaultdict(list)
filepaths = {"/"}
wd = ""
i = 0

cd_pattern = r"\$ cd (.+)"
file_pattern = r"(\d+) (.+)"
dir_pattern = r"(dir) (.+)"


while i < len(lines):
    if cd_match:=re.match(cd_pattern, lines[i]):
        line = lines[i] # We just deal with one line in this case
        changing_to = f"{wd}{cd_match.group(1)}/" if line != "$ cd /" else "/"

        # Handle case where we are going up
        if changing_to.endswith("../"):
            changing_to = wd.rsplit("/", maxsplit=2)[0] + "/"
        
        # If we don't have this filepath yet, add it to the set of filepaths 
        if changing_to not in filepaths:
            print("adding", changing_to)
            filepaths.add(changing_to)

        # Change the file stub, and increment i
        wd = changing_to
        i += 1
    else:
        # Add information to the filesystem at the working directory using the next line if it meets some criteria
        while i+1 < len(lines) and ((file_match:=re.match(file_pattern, lines[i+1])) or (dir_match:=re.match(dir_pattern, lines[i+1]))):
            if file_match:
                # Just add the file size to the working directory for summing
                files[wd].append(int(file_match.group(1)))

                # add the full file name to the filepaths
                filepaths.add(f"{wd}{file_match.group(2)}")
            elif dir_match:
                # add the directory name to the filepaths
                filepaths.add(f"{wd}{dir_match.group(2)}/")
            i += 1
        i += 1

directories = [d for d in filepaths if d.endswith("/")]
dir_sizes = {d: sum([sum(sizes) for name, sizes in files.items() if name.startswith(d)]) for d in directories}

print(sum([size for size in dir_sizes.values() if size <= 100000]))
    
