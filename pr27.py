from tqdm import trange


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def f(a, b):
    def pol(n):
        return n ** 2 + a * n + b

    res = 0

    for n in range(0, 1_000_000):
        if is_prime(pol(n)):
            res += 1
        else:
            break

    return res


max_ = 0
a_ = 0
b_ = 0
for a in trange(-999, 1_000):
    for b in range(-1_000, 1_001):
        t = f(a, b)
        if t > max_:
            max_ = t
            a_, b_ = a, b
print(a_ * b_)
