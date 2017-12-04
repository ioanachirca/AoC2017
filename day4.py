total = 0
lines = [line.rstrip('\n') for line in open('in4.txt')]

for line in lines:	
	words = line.split(" ")
	word_set = set()
	ok = True
	for word in words:
		if word in word_set:
			ok = False
			break
		word_set.add(word)
	if ok is True:
		total += 1

print(total)
