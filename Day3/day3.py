import re
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
			if lines[row-1][cole] != ".":
				print("up right", number)
		
		if cole < len(lines[row]) and row < len(lines) - 1: #down right
			ret |= lines[row+1][cole] != "."
			if lines[row+1][cole] != ".":
				print("down right", number)
		
		if cols > 0 and row > 0: #up left
			ret |= lines[row-1][cols-1] != "."
		
		if cols > 0 and row < len(lines) - 1: #down left
			ret |= lines[row+1][cols-1] != "."

		if ret:
			lines[row] = lines[row][:cols] + "Y" * sl + lines[row][cole:]
			return number
		else:
			lines[row] = lines[row][:cols] + "N" * sl + lines[row][cole:]
			return 0

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]
sum = 0

for i in range(len(lines)):
	matches = re.finditer(r'[0-9]+', lines[i])
	for _, match in enumerate(matches):
		num = check_symbols(lines, i, match.start(), match.end(), int(lines[i][match.start():match.end()]))
		sum += num

for line in lines:
	print(line)
print(sum)

