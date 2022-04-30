target = '1_2_3_4_5_6_7_8_9_0'


def is_good(n):
    n = str(n)
    for i in range(0, len(n), 2):
        if n[i] != target[i]:
            return False
    return True


min_ = int(target.replace('_', '0'))
min_ = int(min_ ** 0.5)

i = min_
i -= 80
it = 0

t = [40, 60]
while True:
    if is_good(i ** 2):
        print(i)
        break
    i += t[it % 2]

    it += 1
