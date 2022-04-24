from tqdm import trange


def eratosphene(n):
    res = list(range(n + 1))
    res[1] = 0
    for i in res:
        if i > 1:
            for j in range(2 * i, len(res), i):
                res[j] = 0
    res = [i for i in res if i != 0]
    return res


primes = eratosphene(3_000_000)

max_ = 0
res = 0
N = 1_000_000

for i in trange(len(primes)):
    if primes[i] > N:
        break
    for j in range(i+max_, len(primes)):
        if sum(primes[i:j + 1]) > N:
            break
        if sum(primes[i:j + 1]) in primes and len(primes[i:j + 1]) > max_:
            max_ = len(primes[i:j + 1])
            res = sum(primes[i:j + 1])
print(res)
