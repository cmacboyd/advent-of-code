with open("./13/input.txt", "r") as f:
	packets = [eval(packet) for packet in f.read().split("\n") if packet]


divider_packets = [[[2]], [[6]]]
packets.extend(divider_packets)


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
			if type(test:=compare_integers(pk1[i], pk2[i])) is bool:
				return test

			# otherwise no conclusion, continue onto next elements

		# Both lists
		elif type(pk1[i]) is list and type(pk2[i]) is list:
			# compare the lists
			if type(test:=compare_packets(pk1[i], pk2[i])) is bool:
				return test

		# One integer, one list
		elif type(pk1[i]) is int:
			if type(test:=compare_packets([pk1[i]], pk2[i])) is bool:
				return test

		elif type(pk2[i]) is int:
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


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if not compare_packets(arr[j], arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
 
 
bubbleSort(packets)
indices = []
for index, pkt in enumerate(packets, 1):
	if pkt in divider_packets:
		indices.append(index)

from functools import reduce
print(reduce(lambda x, y: x*y, indices))
