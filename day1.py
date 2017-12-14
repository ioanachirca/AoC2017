x = input("Enter captcha: ")
lst = [int(i) for i in str(x)]
sum = 0

for i in range(len(lst)):
    #next = (i + 1) % len(lst)
    next = (i + len(lst)/2) % len(lst)
    if lst[i] == lst[next]:
        sum += lst[i]

print(sum)
