from tqdm import trange


def p(n):
    return int(n * (3 * n - 1) / 2)


pentagonals = [p(i) for i in range(1, 10_000)]
set_pentagonals = set(pentagonals)

D = 10 ** 10
for i in trange(len(pentagonals)):
    for j in range(i + 1, len(pentagonals)):
        if pentagonals[i] + pentagonals[j] in set_pentagonals and pentagonals[j] - pentagonals[i] in set_pentagonals and \
                pentagonals[j] - pentagonals[i] < D:
            D = pentagonals[j] - pentagonals[i]
print(D)
