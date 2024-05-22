f = open("input.txt", "r")
lines = f.readlines()
f.close()

seeds = set([int(x) for x in lines[0].split(":")[1].strip().split(" ")])

#seed to soil
ssArr = dict( (x[0], (x[1], x[2].strip())) for x in [y.split(" ") for y in lines[3:19]])
temp = set()
for s in seeds:
	found = False
	for x in lines[3:19]:
		(dest, src, ranger) = [int(y.strip()) for y in x.split(" ")]
		print(dest, src, ranger, s)
		if src <= s < (src + ranger):
			print("found")
			temp.add(dest + (s-src))
			found = True
			break
	if not found:
		temp.add(s)
seeds = temp
print(seeds)

##soil to fertilizer
# sfArr = lines[21:39]
temp = set()
for s in seeds:
	found = False
	for x in lines[21:39]:
		(dest, src, ranger) = [int(y.strip()) for y in x.split(" ")]
		if src <= s < src + ranger:
			print("found")
			temp.add(dest + (s-src))
			found = True
			break
	if not found:
		temp.add(s)
seeds = temp
print(seeds)

# # fertiilzer to water
# fwArr = lines[41:81]
temp = set()
for s in seeds:
	found = False
	for x in lines[41:81]:
		(dest, src, ranger) = [int(y.strip()) for y in x.split(" ")]
		if src <= s < src + ranger:
			print("found")
			temp.add(dest + (s-src))
			found = True
			break
	if not found:
		temp.add(s)
seeds = temp
print(seeds)

# # water to light
# wlArr = lines[83:99]
temp = set()
for s in seeds:
	found = False
	for x in lines[83:99]:
		(dest, src, ranger) = [int(y.strip()) for y in x.split(" ")]
		if src <= s < src + ranger:
			print("found")
			temp.add(dest + (s-src))
			found = True
			break
	if not found:
		temp.add(s)
seeds = temp
print(seeds)

# # light to temperature
# ltArr = lines[101:141]
temp = set()
for s in seeds:
	found = False
	for x in lines[101:141]:
		(dest, src, ranger) = [int(y.strip()) for y in x.split(" ")]
		if src <= s < src + ranger:
			print("found")
			temp.add(dest + (s-src))
			found = True
			break
	if not found:
		temp.add(s)
seeds = temp
print(seeds)

# # temperature to humidity
# thArr = lines[143:181]
temp = set()
for s in seeds:
	found = False
	for x in lines[143:181]:
		(dest, src, ranger) = [int(y.strip()) for y in x.split(" ")]
		if src <= s < src + ranger:
			print("found")
			temp.add(dest + (s-src))
			found = True
			break
	if not found:
		temp.add(s)
seeds = temp
print(seeds)

# # humidity to location
# hlArr = lines[183:]
temp = set()
for s in seeds:
	found = False
	for x in lines[183:]:
		(dest, src, ranger) = [int(y.strip()) for y in x.split(" ")]
		if src <= s < src + ranger:
			print("found")
			temp.add(dest + (s-src))
			found = True
			break
	if not found:
		temp.add(s)
seeds = temp
print(seeds)

seeds = list(seeds)
seeds = sorted(seeds)
print(seeds[0], seeds[-1])

