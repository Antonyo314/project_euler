from tqdm import trange


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_good(a, b):
    if is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a))):
        return True
    else:
        return False


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
set_primes = set(primes)

for p1_ in trange(len(primes)):
    p1 = primes[p1_]
    for p2_ in range(p1_ + 1, len(primes)):
        p2 = primes[p2_]
        if not is_good(p1, p2):
            continue
        for p3_ in range(p2_ + 1, len(primes)):
            p3 = primes[p3_]
            if not (is_good(p1, p3) and is_good(p2, p3)):
                continue
            for p4_ in range(p3_ + 1, len(primes)):
                p4 = primes[p4_]
                if not (is_good(p1, p4) and is_good(p2, p4) and is_good(p3, p4)):
                    continue
                for p5_ in range(p4_ + 1, len(primes)):
                    p5 = primes[p5_]
                    if is_good(p1, p5) and is_good(p2, p5) and is_good(p3, p5) and is_good(p4, p5):
                        print(p1, p2, p3, p4, p5)
                        print(sum([p1, p2, p3, p4, p5]))
print('finish')
