def max_remainder(a):
    res = [2]
    for i in range(1, 100_000_000, 2):
        if i * 2 * a % a ** 2 in res:
            break
        res.append(i * 2 * a % a ** 2)

    return max(res)


result = 0

for i in range(3, 1_001):
    result += max_remainder(i)

print(result)
