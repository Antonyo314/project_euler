from tqdm import trange


def good_n(n):
    res = 0

    for i in str(n):
        res += int(i) ** 5
    if res == n:
        return True
    return False


res = 0
for i in trange(10, 1_000_000):
    if good_n(i):
        res += i

print(res)
# 443839