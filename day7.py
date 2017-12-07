import re

def c_sum(node):
    cumulative = weights[node]
    if node in children:
        cumulative += sum([c_sum(child) for child in children[node]])
    cumulative_weights[node] = cumulative
    return cumulative

def check_sums(node):
    if node not in children:
        print ("we are at leaf " + node)
        print([cumulative_weights[child] for child in children[tree_structure[node]]])
    else:
        child_sum = -1
        ok = True
        for child in children[node]:
            if child_sum == -1:
                child_sum = cumulative_weights[child]
            elif child_sum != cumulative_weights[child]:
                ok = False
                check_sums(child)
        # all child nodes are fine -> current node is the problem
        if ok is True:
            for child in children[tree_structure[node]]:
                print("" + str(cumulative_weights[child]) + " " + str(weights[child]) + " " + str([cumulative_weights[c] for c in children[child]]))




tree_structure = dict()
weights = dict()
children = dict()
root = ''
cumulative_weights = dict()

lines = [line.rstrip('\n') for line in open('day7.txt')]
for line in lines:
    info = re.split(' |, ', line)
    if root == '':
        root = info[0]
    tree_structure[info[0]] = ''
    weights[info[0]] = int(info[1][1:-1])
    if len(info) > 2:
        children[info[0]] = [child for child in info[3:]]
        #print (children[info[0]])

for key in tree_structure:
    if key in children:
        # put key as parent for all the children
        for child in children[key]:
            tree_structure[child] = key

# tree is ready, now only the root will have no parent
# can start from anywhere
while tree_structure[root] != '':
    root = tree_structure[root]

print(root)

# find cumulative weights for all nodes
root_sum = c_sum(root)

check_sums(root)