import sys

lines = [line.rstrip('\n') for line in open('in2.txt')]
checksum = 0

for line in lines:
    row = [int(x) for x in line.split('\t') if x != '']
    #diff = max(row) - min(row)
    diff = 0
    not_found = True
    for i in range(len(row) - 1):
        if not_found is True:
            for j in range (i + 1, len(row)):
                if row[i] % row[j] == 0 or row[j] % row[i] == 0:
                    if row[i] > row[j]:
                        diff = row[i] / row[j]
                    else:
                        diff = row[j] / row[i]
                    print(str(row[i]) + ' ' + str(row[j]))
                    not_found = False
                    break

    checksum += diff

print(checksum)