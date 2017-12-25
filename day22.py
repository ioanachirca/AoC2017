#g = ['..#', '#..', '...']

g = [line.rstrip('\n') for line in open('in22.txt')]

grid = {}

# infinite grid is stored in dictionary
for y in range(len(g)):
    for x in range(len(g[0])):
        if g[y][x] == '#':
            grid[str([x, y])] = g[y][x]

pos = [len(g[0])/2, len(g)/2]
direction = 0 # up
infected = 0

for n in xrange(10000000):
    s = str(pos)
    status = grid.setdefault(s, '.') # similiar to getdefault...

    if status == '.':
        direction = (direction - 1) % 4 # left
        grid[s] = 'W'
    elif status == 'W':
        grid[s] = '#'
        infected += 1
    elif status == '#':
        direction = (direction + 1) % 4 # right
        grid[s] = 'F'
    elif status == 'F':
        direction = (direction + 2) % 4 # reverse dir
        grid[s] = '.'

    # change direction
    if direction == 0: # up
        pos[1] -= 1
    elif direction == 1: # right
        pos[0] += 1
    elif direction == 2: # down
        pos[1] += 1
    elif direction == 3: # left
        pos[0] -= 1

print infected