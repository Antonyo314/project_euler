def pal(n):
    n = str(n)
    n = n.replace('0', ' ').lstrip().replace(' ', '0')
    res = True
    for i in range(int(len(n) / 2)):
        if n[i] != n[-i - 1]:
            res = False
            break
    return res


result = 0
for i in range(1_000_000):
    if pal(i) and pal('{0:b}'.format(i)):
        result += i

print(result)
