from tqdm import trange


def f(n, m):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += (n + 1 - i) * (m + 1 - j)

    return res


min_ = 1e20
res = 0
for n in trange(1, 1_000_000):

    for m in range(1, 1_000_000):
        t = f(n, m)
        if t > 2_000_000:
            break
        if abs(t - 2_000_000) < min_:
            min_ = abs(t - 2_000_000)
            res = n * m
    if f(n, 1) > 2_000_000:
        break
print(res)
