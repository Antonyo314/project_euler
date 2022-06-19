def eratosphene(n):
    res = list(range(n + 1))
    res[1] = 0
    for i in res:
        if i > 1:
            for j in range(2 * i, len(res), i):
                res[j] = 0
    res = [i for i in res if i != 0]
    return res


primes = eratosphene(10_000)

primes = [p for p in primes if len(str(p)) == 4]

d = {}

for p in primes:
    t = ''.join([str(j) for j in sorted([int(i) for i in str(p)])])
    if t in d:
        d[t].append(p)
    else:
        d[t] = [p]

d = {k: v for k, v in d.items() if len(v) >= 3}

for v in d.values():

    for a, b, c in zip(v, v[1:], v[2:]):
        if b - a == c - b:
            print(str(a) + str(b) + str(c))
#This is not a complete solution. The numbers might not be neighbors. Just in this case we were lucky!!!