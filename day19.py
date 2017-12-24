lines = [line.rstrip('\n') for line in open('in19.txt')]
grid = [[c for c in line] for line in lines]

current_y = grid[0].index('|')
current_x = 0
direction = 'down'
message = []
steps = 0

while grid[current_x][current_y] != ' ':
    steps += 1
    if direction == 'down':
        current_x += 1
    elif direction == 'up':
        current_x -= 1
    elif direction == 'left':
        current_y -= 1
    elif direction == 'right':
        current_y += 1
    if grid[current_x][current_y] == '+':
        if direction in ['down', 'up']:
            if current_y + 1 < len(grid[0]) and grid[current_x][current_y+1] != ' ':
                direction = 'right'
            else:
                direction = 'left'
        else:
            if current_x + 1 < len(grid) and grid[current_x+1][current_y] != ' ':
                direction = 'down'
            else:
                direction = 'up'
    elif grid[current_x][current_y] not in ['|', '-', ' ']:
        message.append(grid[current_x][current_y])

print ''.join(message)
print steps