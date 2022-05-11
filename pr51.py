from tqdm import trange
from time import time


def eratosphene(n):
    res = list(range(n + 1))
    res[1] = 0
    for i in res:
        if i > 1:
            for j in range(2 * i, len(res), i):
                res[j] = 0
    res = [i for i in res if i != 0]
    return res


primes = eratosphene(1_000_000)
print(len(primes))

arr = {}
for i in range(1, 20):
    arr[i] = [prime for prime in primes if len(str(prime)) == i]


def is_good(n, prime):
    n = str(n)
    prime = str(prime)
    if ('0' in n and len(set(n)) == 2) or ('0' not in n and len(set(n)) == 1):
        for i in range(len(n)):
            if int(n[-(i + 1)]) + int(prime[-(i + 1)]) > 9:
                return False
        temp = []
        for i in range(len(n)):
            if n[-(i + 1)] != '0':
                temp.append(prime[-(i + 1)])
        if len(set(temp)) > 1:
            return False
        return True
    else:
        return False


def f(n):
    t = [i for i in str(n) if i != '0']
    t = int(t[0])
    return int(n / t)


def find_solution(N):
    for i in trange(5, 20):
        for prime in arr[i]:
            temp_primes = [i - prime for i in arr[i]]
            temp_primes = [i for i in temp_primes if is_good(i, prime)]
            temp_primes = [f(i) for i in temp_primes]
            d_counter = {}
            for a in temp_primes:
                if a not in d_counter:
                    d_counter[a] = 0
                d_counter[a] += 1
            try:
                if d_counter[max(d_counter, key=d_counter.get)] == N - 1:
                    return prime
            except:
                pass


s = time()
print(find_solution(8))
print(time() - s)
