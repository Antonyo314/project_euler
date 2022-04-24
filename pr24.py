def fact(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i

        return res


def f(n, m):
    m -= 1
    l = list(range(n))
    res = ''
    while m != 0:
        res += str(l[m // fact(n - 1) + (m % fact(n) > 0) - 1])
        l.remove(l[m // fact(n - 1) + (m % fact(n) > 0) - 1])
        m -= (m // fact(n - 1) + (m % fact(n) > 0) - 1) * fact(n - 1)
        n -= 1
    res += str(l[0])
    return res


print(f(10, 1_000_000))
