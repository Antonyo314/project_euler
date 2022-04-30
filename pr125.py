from tqdm import trange
def is_palindromic(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            return False
    return True


N = 1_000_000_00

result = []
for i in trange(1, int(N ** 0.5)):
    for j in range(i + 1, int(N ** 0.5)):
        if sum([a**2 for a in range(i, j + 1)]) > N:
            break
        if is_palindromic(sum([a**2 for a in range(i, j + 1)])):
            result.append(sum([a**2 for a in range(i, j + 1)]))


print(sum(set(result)))