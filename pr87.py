from tqdm import tqdm


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

s = set()
for p1 in tqdm(primes):
    if p1 ** 2 > 50_000_000:
        break
    for p2 in primes:
        if p1 ** 2 + p2 ** 3 > 50_000_000:
            break
        for p3 in primes:
            if p1 ** 2 + p2 ** 3 + p3 ** 4 > 50_000_000:
                break
            s.add(p1 ** 2 + p2 ** 3 + p3 ** 4)
print(len(s))
