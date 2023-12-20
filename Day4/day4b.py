f = open("input.txt", "r")
lines = f.readlines()
copies = [1 for x in lines]
points = 0
for i, line in enumerate(lines):
	line = line.split(":")[1].strip()
	[winners, numbers] = line.split("|")
	winners = set([x.strip() for x in winners.split(" ") if x != ""])
	numbers = set([x.strip() for x in numbers.split(" ") if x != ""])
	myWinners = list(winners.intersection(numbers))

	numWinners = len(myWinners)
	if numWinners > 0:
		points += 2**(numWinners - 1)

		for j in range(i+1, i+numWinners+1):
			copies[j] += copies[i]
print("Points", points)
numCopies = 0
for i in range(len(copies)):
	numCopies += copies[i]
print("Copies", copies, numCopies)