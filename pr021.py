def proper_divisors(n):
    if n <= 0:
        return 0
    res = 0
    for i in range(1, n):
        if n % i == 0:
            res += i

    return res


print(proper_divisors(220))
print(proper_divisors(284))


res = 0
for i in range(1, 10_000):
    a = proper_divisors(i)
    if proper_divisors(a) == i and a != i:
        res += i

print(res)
