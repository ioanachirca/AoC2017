h = 0

b = 65
b *= 100
b += 100000
c = b + 17000

def is_composite(x):
    i = 2
    while i < x / 2:
        if x % i == 0:
            return True
        i += 1
    return False

for x in xrange(b, c+1, 17):
    if is_composite(x):
        h += 1

print h