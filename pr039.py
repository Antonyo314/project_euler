from tqdm import trange


def f(p):
    res = 0
    for a in range(1, p):
        for b in range(a, p):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                res += 1
    return res


max_ = 0
res = 0
for p in trange(3, 1_000 + 1):
    t = f(p)
    if t > max_:
        max_ = t
        res = p

print(res)
