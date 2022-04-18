from tqdm import trange


def f(a, b):
    res = ''
    for i in b:
        res += str(a * i)
    return int(res)


def is_pandigital(n):
    if len(str(n)) == 9 and len([i for i in str(n)]) == len(set([i for i in str(n)])) and '0' not in str(n):
        return True
    else:
        return False


max_ = 0

arr = [list(range(1, i + 1)) for i in range(2, 10)]

for i in trange(1, 99999):
    for k in arr:
        temp = f(i, k)
        if len(str(temp)) > 9:
            break
        if is_pandigital(temp):
            max_ = max(max_, temp)
print(max_)
