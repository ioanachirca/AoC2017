def exchange(i, j, index_to_name, name_to_index):
    # swap by index
    name_to_index[index_to_name[i]] = j
    name_to_index[index_to_name[j]] = i 
    tmp = index_to_name[i]
    index_to_name[i] = index_to_name[j]
    index_to_name[j] = tmp
    
def partner(name1, name2, index_to_name, name_to_index):
    # swap by name - find indexes and then swap by them
    index1 = name_to_index[name1]
    index2 = name_to_index[name2]
    exchange(index1, index2, index_to_name, name_to_index)

def spin(number, index_to_name, name_to_index):
    # take last number els and move them in the front
    tmp = index_to_name[size-number:] + index_to_name[:size-number]
    for i in range(size):
        index_to_name[i] = tmp[i]
    for i in range(size):
        name_to_index[index_to_name[i]] = i

def execute_move(move, index_to_name, name_to_index):
    if move.startswith('s'):
        spin(int(move[1:]), index_to_name, name_to_index)
    elif move.startswith('x'):
        info = move[1:].split('/')
        exchange(int(info[0]), int(info[1]), index_to_name, name_to_index)
    elif move.startswith('p'):
        info = move[1:].split('/')
        partner(info[0], info[1], index_to_name, name_to_index)

name_to_index = dict()
index_to_name = []
size = 16

for i in range(size):
    letter = chr(ord('a') + i)
    index_to_name.append(letter)
    name_to_index[letter] = i

with open('in16.txt') as f:
    moves = f.readline().strip('\n').split(',')

configurations = set()
configurations.add(''.join(index_to_name))

stop = 0
billion = 1000000000
for i in xrange(billion):
    stop += 1
    for move in moves:
        execute_move(move, index_to_name, name_to_index)
    # did the dance, now check if this position has been seen before
    config = ''.join(index_to_name)
    if config in configurations:
        print("After " + str(i) + " list is " + str(index_to_name) + " already seen!")
        break

cycles = billion/stop
extra_iterations = billion - stop * cycles

for i in xrange(extra_iterations):
    for move in moves:
        execute_move(move, index_to_name, name_to_index)

print ''.join(index_to_name)
