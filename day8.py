import sys

def check_condition(reg, comparator, value):
    if comparator == '==':
        return registers[reg] == value
    elif comparator == '<':
        return registers[reg] < value
    elif comparator == '<=':
        return registers[reg] <= value
    elif comparator == '>':
        return registers[reg] > value
    elif comparator == '>=':
        return registers[reg] >= value
    elif comparator == '!=':
        return registers[reg] != value
    return False

instructions = [line.rstrip('\n') for line in open('day8.txt')]

registers = dict()
max_ever = -sys.maxint - 1

for instruction in instructions:
    line = instruction.split(' ')
    reg1 = line[0]
    op = line[1]
    val1 = int(line[2])
    reg2 = line[4]
    comp = line[5]
    val2 = int(line[6])
    # first check condition
    if reg2 not in registers:
        registers[reg2] = 0
    if reg1 not in registers:
        registers[reg1] = 0
    if check_condition(reg2, comp, val2):
        if op == 'inc':
            registers[reg1] = registers[reg1] + val1
        elif op == 'dec':
            registers[reg1] = registers[reg1] - val1
        if registers[reg1] > max_ever:
            max_ever = registers[reg1]


max_value = -sys.maxint - 1
for key, val in registers.iteritems():
    if val > max_value:
        max_value = val

print(max_value)
print(max_ever)
    
