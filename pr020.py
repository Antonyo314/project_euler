def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


s = str(fact(100))

res = 0

for i in s:
    res += int(i)

print(res)
