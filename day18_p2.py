import collections
import multiprocessing.pool
import queue

instructions = [line.rstrip('\n') for line in open('in18.txt')]

def run_thread(id, in_queue, out_queue):
    registers = collections.defaultdict(lambda : id)
    program_counter = 0
    count = 0

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
        elif instr == 'add':
            registers[reg] += value(info[2])
        elif instr == 'mul':
            registers[reg] *= value(info[2])
        elif instr == 'mod':
            registers[reg] %= value(info[2])
        elif instr == 'snd':
            out_queue.put(value(info[1]))
            count += 1
        elif instr == 'rcv':
            try: # this prevents deadlock
                registers[reg] = in_queue.get(timeout=5)
            except queue.Empty:
                return count
        elif instr == 'jgz':
            if value(reg) > 0:
                program_counter += value(info[2])
                continue
        program_counter += 1

thread_pool = multiprocessing.pool.ThreadPool(2)

q1 = multiprocessing.Queue()
q2 = multiprocessing.Queue()

result1 = thread_pool.apply_async(run_thread, (0, q1, q2))
result2 = thread_pool.apply_async(run_thread, (1, q2, q1))

print(result2.get())