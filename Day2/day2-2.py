f = open("input.txt", "r")
lines = f.readlines()
sum = 0
for line in lines:
	line = line.strip()
	game = line.split(":")
	rounds = game[1].split(";")
	rounds = [round.strip() for round in rounds]
	full_rounds = []
	for round in rounds:
		#split on comma
		colors = round.split(",")
		#strip extra whitespace
		colors = [color.strip() for color in colors]
		#split on space
		colors = [color.split(" ") for color in colors]
		colors = [color for sublist in colors for color in sublist]
		full_rounds.extend(colors)
		print(colors)

	print(full_rounds)
	#find smallest of each color
	red = 0
	green = 0
	blue = 0
	for i in range(0, len(full_rounds), 2):
		if full_rounds[i+1] == "red" and int(full_rounds[i]) > red:
			red = int(full_rounds[i])
		elif full_rounds[i+1] == "green" and int(full_rounds[i]) > green:
			green = int(full_rounds[i])
		elif full_rounds[i+1] == "blue" and int(full_rounds[i]) > blue:
			blue = int(full_rounds[i])

	red = max(red, 1)
	blue = max(blue, 1)
	green = max(green, 1)
	print (red, green, blue, round)
	sum += red * green * blue

print(sum)
		
				