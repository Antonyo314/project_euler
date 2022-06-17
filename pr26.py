from tqdm import trange


def f(a, b, res=[]):
    if (a, b) in res:
        return res, (a, b)
    res.append((a, b))

    a *= 10

    if a % b == 0:
        return [], None
    else:
        return f(a % b, b)


max_ = 0
d = -1
for i in trange(1, 1001):
    arr, el = f(1, i)
    if not el:
        continue
    if len(arr) - arr.index(el) > max_:
        max_ = len(arr) - arr.index(el)
        d = i
print(d)
