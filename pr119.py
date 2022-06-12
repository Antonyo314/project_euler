from tqdm import trange


def digit_sum(n):
    n = str(n)
    return sum([int(a) for a in n])


def is_power(a, b):
    while True:
        if a != 1 and b == 1:
            return False
        if a % b != 0:
            return False
        a /= b
        if a == 1:
            return True


def is_good(a):
    return is_power(a, digit_sum(a))


result = list()
for i in range(1, 100):
    for j in range(1, 100):
        result.append(i ** j)
result = [i for i in result if i >= 11]
result = sorted(list(set(result)))
result = [i for i in result if is_good(i)]

print(result[29])
