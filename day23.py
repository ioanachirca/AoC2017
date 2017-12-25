import collections

instructions = [line.rstrip('\n') for line in open('in23.txt')]

def run():
    registers = collections.defaultdict(lambda : 0)
    program_counter = 0
    mul_count = 0

    def value(v):
        if v >= 'a' and v <= 'z':
            val = registers[v]
        else:
            val = int(v)
        return val

    while program_counter < len(instructions):
        info = instructions[program_counter].split(' ')
        instr = info[0]
        reg = info[1]
        if instr == 'set':
            registers[reg] = value(info[2])
        elif instr == 'sub':
            registers[reg] -= value(info[2])
        elif instr == 'mul':
            registers[reg] *= value(info[2])
            mul_count += 1
        elif instr == 'jnz':
            if value(reg) != 0:
                program_counter += value(info[2])
                continue
        program_counter += 1

    print mul_count

run()