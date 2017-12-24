enough = False

def execute_instr(instruction, idx):
    global enough, registers, last_played
    info = instruction.split(' ')
    instr = info[0]
    reg = info[1]
    last_idx = idx
    if reg not in registers:
        registers[reg] = 0
    if instr == 'set':
        if info[2] >= 'a' and info[2] <= 'z':
            value = registers[info[2]]
        else:
            value = int(info[2])
        registers[reg] = value
        idx += 1
    elif instr == 'add':
        if info[2] >= 'a' and info[2] <= 'z':
            value = registers[info[2]]
        else:
            value = int(info[2])
        registers[reg] += value
        idx += 1
    elif instr == 'mul':
        if info[2] >= 'a' and info[2] <= 'z':
            value = registers[info[2]]
        else:
            value = int(info[2])
        registers[reg] *= value
        idx += 1
    elif instr == 'mod':
        if info[2] >= 'a' and info[2] <= 'z':
            value = registers[info[2]]
        else:
            value = int(info[2])
        registers[reg] %= value
        idx += 1
    elif instr == 'jgz':
        if registers[reg] > 0:
            idx += int(info[2])
        else:
            idx += 1
    elif instr == 'snd':
        last_played[reg] = registers[reg]
        idx += 1
    elif instr == 'rcv':
        if reg not in last_played:
            last_played[reg] = 0
        if last_played[reg] > 0 and registers[reg] > 0:
            print 'YAY ' + str(last_played[reg])
            enough = True
        idx += 1

    #print("After " + instructions[last_idx] + " a = " + str(registers['a']) + ", idx = " + str(idx))
    return idx

   
instructions = [line.rstrip('\n') for line in open('in18.txt')]

registers = dict()
last_played = dict()

idx = 0

while enough is False and idx < len(instructions):
    idx = execute_instr(instructions[idx], idx)
    
