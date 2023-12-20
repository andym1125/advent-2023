f = open("input.txt", "r")
lines = f.readlines()

points = 0
for line in lines:
	line = line.split(":")[1].strip()
	[winners, numbers] = line.split("|")
	winners = set([x.strip() for x in winners.split(" ") if x != ""])
	numbers = set([x.strip() for x in numbers.split(" ") if x != ""])
	myWinners = list(winners.intersection(numbers))

	if len(myWinners) > 0:
		points += 2**(len(myWinners) - 1)
print("Points", points)