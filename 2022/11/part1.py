from typing import List, Callable
import re
from functools import reduce

with open("./11/input.txt", "r") as f:
	text = f.read()


monkey_text_list = text.split("\n\n")

# Example monkey
# Monkey 0: 					# monkey unique integer identifier
#   Starting items: 79, 98 		# lists the worry level of each item this monkey starts with
#   Operation: new = old * 19 	# shows how your worry level changes as that monkey inspects an item.
#   Test: divisible by 23 		# shows how the monkey uses your worry level to decide where to throw an item next
#     If true: throw to monkey 2
#     If false: throw to monkey 3

class Monkey:
	def __init__(self, number: int, starting_items:List[int]=[], operation: Callable = lambda x: x, true_monkey: int = -5, false_monkey: int = -5, divisible_by: int = -1000):
		self.number = number
		self.items = starting_items
		self.operation = operation
		self.divisible_by = divisible_by
		self.true_monkey = true_monkey
		self.false_monkey = false_monkey
		self.inspect_count = 0

	def __str__(self):
		return f"Monkey {self.number}: {', '.join([str(i) for i in self.items])}"

	def test(self, to_test):
		if to_test % self.divisible_by == 0:
			return self.true_monkey
		else:
			return self.false_monkey

	def inspect(self):
		for i in range(len(self.items)):
			old_item = self.items[i]
			self.items[i] = self.operation(self.items[i])
			new_item = self.items[i]
			print(f"\tMonkey inspects an item with a worry level {old_item} -> {new_item}")
			self.inspect_count += 1

	def relieve(self):
		for i in range(len(self.items)):
			self.items[i] = self.items[i] // 3
			print(f"\tMonkey gets bored with item. Worry level is divided by 3 to {self.items[i]}")

	def throw_items(self):
		for i in range(len(self.items)):
			# yield the target monkey number, and the item to throw
			throw_to_monkey = self.test(self.items[0])
			throw_item = self.items.pop(0)
			print(f"\tItem with worry level {throw_item} is thrown to monkey {throw_to_monkey}")
			yield throw_to_monkey, throw_item

	def catch_item(self, item):
		self.items.append(item)


# setup the list of monkeys
monkey_pattern = r"Monkey (\d+):\n  Starting items: ([ ,\d]+)\n  Operation: ([^\n]+)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)"
monkey_list = []
for monkey_text in monkey_text_list:
	monkey_match = re.match(monkey_pattern, monkey_text)
	monkey_id, starting_items, operation, divisible_by, true_monkey, false_monkey = monkey_match.groups()

	this_monkey = Monkey(
		int(monkey_id), 
		starting_items=[int(x) for x in starting_items.split(", ")],
		operation=eval(f"lambda old: {operation.split(' = ')[-1]}"), # this is dank lol
		true_monkey = int(true_monkey),
		false_monkey = int(false_monkey),
		divisible_by= int(divisible_by)
	)


	monkey_list.append(this_monkey)


# After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item 
# causes your worry level to be divided by three and rounded down to the nearest integer.

# The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding one at a 
# time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a round.

# When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round with no items could 
# end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.

print("Starting")
print("\n".join([str(monkey) for monkey in monkey_list]))

for round in range(1, 21): # twenty rounds
	print(f"round {round}")
	for monkey in monkey_list:
		print(f"processing monkey {monkey.number}")

		# inspect
		monkey.inspect()

		# relieve
		monkey.relieve()

		# throw items
		for target_monkey, item in monkey.throw_items():
			
			monkey_list[target_monkey].catch_item(item)

		# print("\n".join([str(monkey) for monkey in monkey_list]))
		print("\n")

	print(f"end round {round}")
	print("\n".join([str(monkey) for monkey in monkey_list]))


print("\n")
print("The answer is:")
print(reduce(lambda x,y : x*y, sorted([m.inspect_count for m in monkey_list], reverse=True)[:2]))
