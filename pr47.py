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


N = 1_000_000

primes = eratosphene(N)


def prime_factors(n):
    res = []
    for p in primes:
        if p > n:
            break
        while n % p == 0:
            n /= p
            res.append(int(p))
    return list(set(res))


for a, b, c, d in tqdm(zip(range(N), range(1, N), range(2, N), range(3, N))):
    a_prime_factors = prime_factors(a)
    b_prime_factors = prime_factors(b)
    c_prime_factors = prime_factors(c)
    d_prime_factors = prime_factors(d)

    if len(a_prime_factors) == len(b_prime_factors) == len(c_prime_factors) == len(d_prime_factors) == 4:
        print(a)
        break
