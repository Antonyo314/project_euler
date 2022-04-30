from tqdm import trange


def fact(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i

        return res


def f(a, l=[]):
    l.append(a)
    a = sum([fact(int(i)) for i in str(a)])
    if len(l) > 60:
        return 61
    if a in l:
        return len(l)
    else:
        return f(a, l)


result = 0

for i in trange(1, 1_000_000):
    if f(i, []) == 60:
        result += 1
print(result)
