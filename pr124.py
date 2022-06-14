from tqdm import trange


def eratosphene(n):
    arr = list(range(n + 1))
    arr[1] = 0

    for i in range(2, len(arr)):
        for j in range(i * 2, len(arr), i):
            arr[j] = 0
    arr = [i for i in arr if i != 0]
    return arr


primes = eratosphene(100_000)


def rad(n):
    factors = 1
    if n in primes:
        return n
    for p in primes:
        if n % p == 0:
            factors *= p
    return factors


res_d = dict()
for i in trange(1, 100_000 + 1):
    res_d[i] = rad(i)

res_d = {k: v for k, v in sorted(res_d.items(), key=lambda item: item[1])}

print(list(res_d.keys())[10_000 - 1])
