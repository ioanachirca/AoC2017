def distance(x, y):
    return max(abs(x), abs(y), abs(x+y))

with open('in11.txt') as f:
    moves = f.readline().strip('\n').split(',')

dirs = {"n": (0, 1),"s": (0, -1), "ne": (0.5, 0.5), "sw": (-0.5, -0.5), "nw": (-0.5, 0.5), "se": (0.5, -0.5), }

current_x = 0
current_y = 0
max_dist = 0

for move in moves:
    current_x += dirs[move][0]
    current_y += dirs[move][1]
    max_dist = max(max_dist, distance(current_x, current_y))

print("last distance: " +  str(distance(current_x, current_y)))
print("max distance: " +  str(max_dist))