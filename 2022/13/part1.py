with open("./13/input.txt", "r") as f:
	packet_pairs = [[eval(packet) for packet in pair.split("\n")] for pair in f.read().split("\n\n")]


def compare_integers(a, b):
	if a < b:
		# they are in the right order
		return True
			
	elif a > b:
		# they are in the wrong order
		return False

	else:
		return None


def compare_packets(pk1, pk2):
	i = 0
	while i < len(pk1):
		if i >= len(pk2):
			return False # We got to end of pk2, pk1 is longer, not right order
			

		# Both integers
		elif type(pk1[i]) is int and type(pk2[i]) is int:
			# compare the integers
			print(f"\t- Compare {pk1[i]} vs {pk2[i]}")
			if type(test:=compare_integers(pk1[i], pk2[i])) is bool:
				return test

			# otherwise no conclusion, continue onto next elements

		# Both lists
		elif type(pk1[i]) is list and type(pk2[i]) is list:
			print(f"\t- Compare {pk1[i]} vs {pk2[i]}")
			# compare the lists
			if type(test:=compare_packets(pk1[i], pk2[i])) is bool:
				return test

		# One integer, one list
		elif type(pk1[i]) is int:
			print(f"\t- Compare {[pk1[i]]} vs {pk2[i]}")
			if type(test:=compare_packets([pk1[i]], pk2[i])) is bool:
				return test

		elif type(pk2[i]) is int:
			print(f"\t- Compare {pk1[i]} vs {[pk2[i]]}")
			if type(test:=compare_packets(pk1[i],[pk2[i]])) is bool:
				return test

		# inconclusive, go to next element
		i += 1

	# If we get to end of list pk1 without ending pk2 we are in right order
	if len(pk1) == len(pk2):
		# inconclusive
		return None
	elif len(pk1) < len(pk2):
		return True


correct_indices = []
for index, (left, right) in enumerate(packet_pairs, 1):
	print(f"== Pair {index} ==")
	print(f"- Compare {left} vs {right}")
	if compare_packets(left, right) is True:
		print("\t\t- Left side is smaller, so inputs are in the right order\n")
		correct_indices.append(index)
	elif compare_packets(left, right) is False:
		print("\t\t- Right side is smaller, so inputs are not in the right order\n")

print(correct_indices)
print(sum(correct_indices))

