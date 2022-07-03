from tqdm import trange

N = 10 ** 6

d = dict()
for numerator in trange(1, N):
    denominator = numerator * 7 / 3
    denominator = int(denominator) + 1
    if denominator > N:
        break
    if numerator / denominator < 3 / 7:
        d[numerator / denominator] = f'{numerator}/{denominator}'

print(d[max(d.keys())])
print(d[max(d.keys())].split('/')[0])
