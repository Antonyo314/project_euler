from tqdm import trange


def euclid(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return euclid(a % b, b)
    if b > a:
        return euclid(a, b % a)


N = 12_000
all_fractions_set = set()

for numerator in trange(2, N):
    denominator1 = int(numerator * 3) - 1
    denominator2 = int(numerator * 2) + 1

    for denominator in range(denominator2, denominator1 + 1):
        if denominator > N:
            break
        hcf = euclid(numerator, denominator)

        numerator_ = int(numerator / hcf)
        denominator_ = int(denominator / hcf)

        all_fractions_set.add(f'{numerator_}/{denominator_}')

print(len(all_fractions_set))
