import re

lines = [line.rstrip('\n') for line in open('day12.txt')]
graph = {}

for line in lines:
    info = re.split(' |, ', line)
    graph[info[0]] = info[2:]



groups = 0
all_visited = set()

for n in graph:
    if n not in all_visited:
        # DFS
        visited = set()
        root = n
        stack = [root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                all_visited.add(node)
                stack.extend([x for x in graph[node] if x not in visited])

        print('Node ' + n + ' has a group of ' + str(len(visited)))
        groups += 1

print(str(groups) + ' groups')