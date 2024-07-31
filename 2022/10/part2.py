with open("./10/input.txt", "r") as f:
	instructions = (line.strip() for line in f.readlines())


x = 1
CRT = "" # start with flat CRT

def get_sprite(register):
	sprite = [register-1, register, register+1]
	#print(f"Sprite position:   {''.join(['.' if i not in sprite else '#' for i in range(40)])}")
	return sprite

sprite = get_sprite(x)
cycle = 1

def draw_pixel(cycle, sprite, CRT):
	if ((cycle-1) % 40) in sprite:
		return CRT + "#"
	else:
		return CRT + "."


for this_instruction in instructions:
	if this_instruction == "noop":
		CRT = draw_pixel(cycle, sprite, CRT)
	elif this_instruction.startswith("addx"):
		addx, to_add = this_instruction.split(' ')
		
		#print(f"Start cycle\t{cycle}: begin executing {this_instruction}")
		CRT = draw_pixel(cycle, sprite, CRT)
		#print(f"During cycle\t{cycle}: CRT draws pixel in position {cycle-1}")
		#print(f"Current CRT Row  : {CRT}")
		#print("\n")
		cycle += 1


		CRT = draw_pixel(cycle, sprite, CRT)
		#print(f"During cycle\t{cycle}: CRT draws pixel in position {cycle-1}")
		#print(f"Current CRT Row  : {CRT}")

		x += int(to_add)
		#print(f"End of cycle\t{cycle}: finish executing {this_instruction}, (Register X is now {x})")
		sprite = get_sprite(x)
		#print("\n")

	cycle += 1

#print(CRT)


# unravel CRT
start_row = 0
end_row = 40
while end_row <= 240:
	print(CRT[start_row:end_row])
	start_row += 40
	end_row += 40
