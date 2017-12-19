with open('in9.txt') as f:
    stream = f.readline()

total_score = 0
current_score = 0
total_garbage = 0
current_garbage = 0
is_garbage = False
i = 0

while i < len(stream):
    #print ("stream[" + str(i) + "] = " + stream[i])

    if is_garbage is True:
        if stream[i] is '>':
            is_garbage = False
            total_garbage += current_garbage
            current_garbage = 0
        else:
            current_garbage += 1
    elif is_garbage is False and stream[i] is '<':
        is_garbage = True


    if stream[i] is '!':
        if is_garbage is True:
            current_garbage -= 1
        i = i + 2
        continue

    if is_garbage is False:
        if stream[i] is '{':
            current_score += 1
            total_score += current_score
            print ("current score is " + str(current_score) + " total is " + str(total_score))
        elif stream[i] is '}':
            current_score -= 1

    i = i + 1

print total_garbage
print total_score