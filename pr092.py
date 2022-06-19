from tqdm import trange

d = {}


def f(n):
    if n == 1 or n == 89:
        return n
    else:
        return f(sum([int(i) ** 2 for i in str(n)]))


for i in [44, 58]:
    print(i, f(i))

res = 0
for i in trange(1, 10_000_000):
    if f(i) == 89:
        res += 1
print(res)
