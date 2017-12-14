import operator

def reverse(start_index, nr_els):  # do it in O(n) space!!
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


lst = range(256)
with open('day10.txt', 'r') as f:
    line = f.readline()
nums  = [int(x) for x in line.rstrip('\n').split(',')] 
lens = [code for code in bytearray(line.rstrip('\n'), 'ascii')]
#lens = [ord(n) for n in nums]
lens.extend([17, 31, 73, 47, 23])

current_pos = 0
skip_size = 0

for i in range(64):
    for l in lens:
        reverse(current_pos, l)
        current_pos = (current_pos + l + skip_size) % len(lst)
        skip_size += 1
        #print('After len ' + str(l) + ' lst is ' + str(lst))

dense_hash = []
for i in range(16):
    l = lst[i * 16 : (i+1) * 16]
    xor = reduce(operator.xor, l, 0)
    dense_hash.append('%02x'%xor)

print "".join([xor for xor in dense_hash])

