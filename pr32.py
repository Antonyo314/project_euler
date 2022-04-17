from tqdm import trange


def is_good(s):
    arr = [i for i in s]
    if len(arr) == len(set(arr)) == 9 and '0' not in arr:
        return True
    else:
        return False


result = []

for i in trange(1, 987654321):
    if len(str(i)) > 5:
        break
    for j in range(i):

        res = i * j
        s = str(res) + str(i) + str(j)
        if len(s) > 9:
            break
        if is_good(s):
            result.append(res)

print(sum(set(result)))
