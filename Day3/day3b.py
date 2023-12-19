import re

partnums = []

def check_symbols(lines, row, cols, cole, number):
		sl = cole-cols
		ret = False
		if row > 0:
			for i in range (cols, cole):
				ret |= lines[row-1][i] != "."

		if row < len(lines) - 1:
			for i in range (cols, cole):
				ret |= lines[row+1][i] != "."

		if cols > 0:
			ret |= lines[row][cols-1] != "."
		
		if cole < len(lines[row]):
			ret |= lines[row][cole] != "."
		
		if cole < len(lines[row]) and row > 0: #up right
			ret |= lines[row-1][cole] != "."
		
		if cole < len(lines[row]) and row < len(lines) - 1: #down right
			ret |= lines[row+1][cole] != "."
		
		if cols > 0 and row > 0: #up left
			ret |= lines[row-1][cols-1] != "."
		
		if cols > 0 and row < len(lines) - 1: #down left
			ret |= lines[row+1][cols-1] != "."

		if ret:
			lines[row] = lines[row][:cols] + "Y" * sl + lines[row][cole:]
			partnums.append((number, row, cols, cole))
			return number
		else:
			lines[row] = lines[row][:cols] + "N" * sl + lines[row][cole:]
			return 0

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]
sum = 0

# find all part numbers, and store them in partnums
for i in range(len(lines)):
	matches = re.finditer(r'[0-9]+', lines[i])
	for _, match in enumerate(matches):
		num = check_symbols(lines, i, match.start(), match.end(), int(lines[i][match.start():match.end()]))
		sum += num

# find each *, and for each one determine if exactly 2 part nums are nearby
print(partnums)
sumgearratio = 0
for i in range(len(lines)):
	matches = re.finditer(r"\*", lines[i])
	# find all adj part nums
	# only if num intersects box
	# ie left < end <= right or left <= start <= right and (row == top or row == middle or row == bottom)
	for _, match in enumerate(matches):
		#for readability
		left = match.start()-1
		right = match.end()
		top = i-1
		bottom = i+1
		middle = i

		gearmatches = []
		# partnums.append((number, row, cols, cole))
		for part in partnums:
			if (part[1] == top or part[1] == middle or part[1] == bottom) and (left < part[3] <= right or left <= part[2] <= right):
				gearmatches.append(part[0])
		if len(gearmatches) == 2:
			sumgearratio += gearmatches[0]*gearmatches[1]
			lines[i] = lines[i][:match.start()] + "G" + lines[i][match.start()+1:]


# print edited manual for debugging
for line in lines:
	print(line)
print("Sum", sum)
print("Gear ratio sum", sumgearratio)

