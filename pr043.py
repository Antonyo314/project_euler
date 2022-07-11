from itertools import permutations
from tqdm import tqdm

perms = permutations([i for i in range(10)])

res = 0
for perm in tqdm(list(perms)):
    a = ''.join([str(p) for p in perm])
    if int(a[0]) == 0:
        continue
    if int(a[3]) % 2 != 0:
        continue
    if int(a[2:5]) % 3 != 0:
        continue
    if int(a[5]) % 5 != 0:
        continue
    if int(a[4:7]) % 7 != 0:
        continue
    if int(a[5:8]) % 11 != 0:
        continue
    if int(a[6:9]) % 13 != 0:
        continue
    if int(a[7:10]) % 17 != 0:
        continue
    res += int(a)

print(res)
