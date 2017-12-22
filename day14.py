import operator
import sys
sys.setrecursionlimit(10000)

def dec2bin(number):
    binval = format(number, '08b')
    """
    while len(binval) < 8:
        binval = '0' + binval"""
    return binval

def reverse(start_index, nr_els, lst):  # do it in O(n) space!!
    if nr_els == 1:
        return
    tmp = []
    s_i = start_index
    for i in range(nr_els):
        tmp.append(lst[s_i])
        s_i = (s_i + 1) % len(lst)
    tmp = tmp[::-1]
    s_i = start_index
    for i in range(nr_els):
        lst[s_i] = tmp[i]
        s_i = (s_i + 1) % len(lst)

def knot_hash(string, lst):
    lens = [code for code in bytearray(string, 'ascii')]
    lens.extend([17, 31, 73, 47, 23])

    current_pos = 0
    skip_size = 0

    for i in range(64):
        for l in lens:
            reverse(current_pos, l, lst)
            current_pos = (current_pos + l + skip_size) % len(lst)
            skip_size += 1
            #print('After len ' + str(l) + ' lst is ' + str(lst))

    dense_hash = []
    for i in range(16):
        l = lst[i * 16 : (i+1) * 16]
        xor = reduce(operator.xor, l, 0)
        #dense_hash.append('%02x'%xor) #this should now be binary
        dense_hash.append(xor)

    #return "".join([xor for xor in dense_hash])
    return ''.join(dec2bin(x) for x in dense_hash)
    #return ''.join(['%08b'%x for x in dense_hash])

def count_ones(string):
    total = 0
    for c in string:
        if c is '1':
            total += 1
    return total


used = 0
grid = []
for i in range(128):
    lst = range(256)
    khash = knot_hash('flqrgnkx-' + str(i), lst)
    #print khash
    used += count_ones(khash)
    # construct grid
    grid.append([c for c in khash])

print used

def getRoot(cell):
    while disjointSet[cell] != cell:
        cell = disjointSet[cell]
    return cell

disjointSet = dict()
islands = 0

for i in range(128):
    for j in range(128):
        if grid[i][j] == '1':
            cell = (i, j)
            north = ()
            west = ()
            if j > 0 and grid[i][j-1] == '1':
                west = (i, j-1)
            if i > 0 and grid[i-1][j] == '1':
                north = (i-1, j)
            if north != () and west != ():
                # two islands nearby, will merge with them
                northRoot = getRoot(north)
                westRoot = getRoot(west)
                print('---------------------------------------')
                print ("north root: " + str(northRoot))
                print ("west root: " + str(westRoot))
                if northRoot != westRoot:
                    print('diff')
                    islands -= 1
                disjointSet[cell] = north
            elif north != ():
                disjointSet[cell] = north
            elif west != ():
                disjointSet[cell] = west
            else:
                disjointSet[cell] = cell
                islands += 1

print islands

def dfs(r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == '0':
        return 0
    grid[r][c] = '0'
    dfs(r+1, c)
    dfs(r, c+1)
    dfs(r-1, c)
    dfs(r, c-1)
    return 1

islands = 0
for i in range(128):
    for j in range(128):
        islands += dfs(i, j)

print islands


