def eratosphene(n):
    res = list(range(n + 1))
    res[1] = 0
    for i in res:
        if i > 1:
            for j in range(2 * i, len(res), i):
                res[j] = 0
    res = [i for i in res if i != 0]
    return res


primes = eratosphene(100_000)

squares = [i ** 2 for i in range(1, 100)]


def f(n):
    for p in primes:
        if p > n:
            return False
        for sq in squares:
            if n == p + 2 * sq:
                return True
            elif n < p + 2 * sq:
                break
    return False


for i in range(9, 100_000, 2):
    if i not in primes:
        if not (f(i)):
            print(i)
            break
