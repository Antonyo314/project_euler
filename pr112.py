def sign(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1


def is_bouncy(n):
    n = [int(i) for i in str(n)]
    signs = []
    for i, j in zip(n, n[1:]):
        signs.append(sign(j - i))
        if -1 in signs and 1 in signs:
            return True
    # if 0 in signs and len(set(signs)) == 1:
    #     return True
    return False


it1 = 0

t = 100

while it1 / t < 0.99:
    t += 1

    if is_bouncy(t):
        it1 += 1

print(t)
