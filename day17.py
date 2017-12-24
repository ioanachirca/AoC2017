lst = [0]
curr = 0
step = 354
####### Part 1 #######
for i in xrange(1, 2018):
    curr = (curr + (step % len(lst)) + 1) % len(lst)
    lst.insert(curr, i)

idx = lst.index(2017)
print lst[(idx + 1) % len(lst)]

####### Part 2 #######
# don't have to generate the list, only know current pos and value after 0 (== val at pos 1)
curr = 0
after_zero = 0
for i in xrange(1, 50000001):
    curr = (curr + step) % i + 1
    if curr == 1:
        after_zero = i

print after_zero