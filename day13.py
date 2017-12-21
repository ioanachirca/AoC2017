def move_scanners():
    # move all scanners one step
    for i in range(len(scanners)):
        if scanners[i] != -1:
            scanners[i] = (scanners[i] + directions[i]) % ranges[i]
            if scanners[i] == 0:
                directions[i] = 1
            elif scanners[i] == ranges[i] - 1:
                directions[i] = -1

lines = [line.rstrip('\n') for line in open('in13.txt')]
ranges = [] # will have max_depth elements
scanners = [] # max_depth_elements
for line in lines:
    info = [int(x) for x in line.split(': ')]
    while info[0] > len(ranges):
        ranges.append(0)
    ranges.append(info[1])

scanners = [0 if x != 0 else -1 for x in ranges ]
print ranges

total_severity = 0
directions = [1] * len(scanners)
delayed = 0
step = -1
while step < len(ranges) - 1:
    step += 1 # currently at scanner with index step
    if scanners[step] == 0:
        total_severity += step * ranges[step]

    # now move all scanners
    move_scanners()



print total_severity
    