from tqdm import tqdm


def eratosphene(n):
    res = list(range(n + 1))
    res[1] = 0
    for i in res:
        if i > 1:
            for j in range(2 * i, len(res), i):
                res[j] = 0
    return res


arr = eratosphene(1_000_000)
primes = [i for i in arr if i != 0]


def l(n):
    n = str(n)
    res = []
    while len(n) > 0:
        res.append(n)
        n = n[1:]
    res = [int(i) for i in res]
    return res


def r(n):
    n = str(n)
    res = []
    while len(n) > 0:
        res.append(n)
        n = n[:-1]
    res = [int(i) for i in res]
    return res


temp = 0
result = 0
for prime in tqdm(primes):
    l_list = l(prime)
    r_list = r(prime)
    res = True
    for i in l_list + r_list:
        if i not in primes:
            res = False
            break
    if res:
        result += prime
        temp += 1
        if temp == 15:
            break
print(result - 2 - 3 - 5 - 7)
# result -= 2 + 3 + 5 + 7
# print(result)
