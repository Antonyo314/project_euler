from tqdm import trange

N = 10 ** 6

d = dict()
for nominator in trange(1, N):
    denominator = nominator * 7 / 3
    if int(denominator) != denominator:
        denominator = int(denominator) + 1
    if denominator > N:
        break
    if nominator / denominator < 3 / 7:
        d[nominator / denominator] = f'{nominator}/{denominator}'

# print(d[max(d.keys())])
print(d[max(d.keys())].split('/')[0])
