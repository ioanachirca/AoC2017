configurations = set()

initial_config = [int(line.rstrip('\n')) for line in open('in6.txt')]
configurations.add(tuple(initial_config))
config_step_dict = dict()
config_step_dict[tuple(initial_config)] = 0
steps = 0

while True:
    # first need to find bank with biggest number of blocks
    biggest_value = -1
    biggest_index = -1
    for i in range(len(initial_config)):
        if initial_config[i] > biggest_value:
            biggest_value = initial_config[i]
            biggest_index = i
    # now redistribute the biggest value amongst the other banks
    idx = (biggest_index + 1) % len(initial_config)
    initial_config[biggest_index] = 0
    while biggest_value > 0:
        initial_config[idx] += 1
        idx = (idx + 1) % len(initial_config)
        biggest_value -= 1
    steps += 1
    # see if current configuration has been seen before
    if tuple(initial_config) in configurations:
        break
    configurations.add(tuple(initial_config))
    config_step_dict[tuple(initial_config)] = steps

print(steps)
print(steps - config_step_dict[tuple(initial_config)])
