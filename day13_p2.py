lines = [line.rstrip('\n') for line in open('in13.txt')]
ranges = [] # will have max_depth elements
scanners = [] # max_depth_elements
for line in lines:
    info = [int(x) for x in line.split(': ')]
    while info[0] > len(ranges):
        ranges.append(0)
    ranges.append(info[1])

scanners = [0 if x != 0 else -1 for x in ranges ]

directions = [1] * len(scanners)
delay = 0
step = -1
while True:
    i = 0
    while i < len(scanners):
        if scanners[i] != -1:
            if (delay + i) % (2 * ranges[i] - 2) == 0:
                break
        i += 1
    if i == len(scanners):
        break
    delay += 1

print delay
    