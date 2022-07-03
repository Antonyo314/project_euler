from tqdm import trange

N = 10 ** 6

d = dict()
for numinator in trange(1, N):
    denominator = numinator * 7 / 3
    denominator = int(denominator) + 1
    if denominator > N:
        break
    if numinator / denominator < 3 / 7:
        d[numinator / denominator] = f'{numinator}/{denominator}'

print(d[max(d.keys())])
print(d[max(d.keys())].split('/')[0])
