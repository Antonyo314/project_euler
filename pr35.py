from tqdm import tqdm


def circulars(n):
    n = str(n)
    res = []
    for i in range(len(n) - 1):
        n = n[-1] + n[:-1]
        res.append(int(n))
    return res


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


result = 0

for prime in tqdm(primes):
    circulars_list = circulars(prime)

    temp_res = True
    for i in circulars_list:
        if i not in primes:
            temp_res = False
            break
    if temp_res:
        result += 1

print(result)
