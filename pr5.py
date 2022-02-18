N = 20


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [i for i in range(2, N + 1) if is_prime(i)]


def f(n, p):
    res = 0
    while True:
        if n % p == 0:
            n /= p
            res += 1
        else:
            break
    return res


prime_dict = {}

for prime in primes:
    prime_dict[prime] = 0

for n in range(1, N + 1):
    for p in primes:
        prime_dict[p] = max(prime_dict[p], f(n, p))

result = 1
for k, v in prime_dict.items():
    result *= k ** v
print(result)
