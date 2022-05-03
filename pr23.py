from tqdm import trange


def n_of_proper_divisors(n):
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += i

            if i ** 2 != n:
                res += n / i

    res -= n

    return int(res)

abundants = []

for i in range(2, 28123):
    if n_of_proper_divisors(i) > i:
        abundants.append(i)

can_be_written_as_sum_of_abundants = []

for i in trange(len(abundants)):
    for j in range(i, len(abundants)):
        can_be_written_as_sum_of_abundants.append(abundants[i] + abundants[j])

can_be_written_as_sum_of_abundants = list(set(can_be_written_as_sum_of_abundants))
result = 0

for i in trange(1, 28123 + 1):
    if i not in can_be_written_as_sum_of_abundants:
        result += i

print(result)
