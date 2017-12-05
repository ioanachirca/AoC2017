offsets = [int(line.rstrip('\n')) for line in open('in5.txt')]

idx = 0
steps = 0

while idx >= 0 and idx < len(offsets):
	jump_to = offsets[idx]
	if jump_to >= 3:
		offsets[idx] -= 1
	else:
		offsets[idx] += 1
	idx += jump_to
	steps += 1

print(steps)