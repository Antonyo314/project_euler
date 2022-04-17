def fact(n):
    res = 1

    for i in range(2, n + 1):
        res *= i
    return res


def good_n(n):
    arr = [int(i) for i in str(n)]
    if sum([fact(i) for i in arr]) == n:
        return True
    else:
        return False


res = 0
for i in range(3, 1_000_000):
    if good_n(i):
        res += i

print(res)
