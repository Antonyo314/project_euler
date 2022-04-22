def factorial(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
    return res


def C(a, b):
    return int(factorial(a) / (factorial(b) * factorial(a - b)))


result = 0

for i in range(1, 101):
    for j in range(1, i + 1):
        if C(i, j) > 1_000_000:
            result += 1

print(result)
