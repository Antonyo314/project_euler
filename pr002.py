res = 0
a, b = 1, 2
while True:
    if a > 4_000_000:
        break

    if a % 2 == 0:
        res += a
    a, b = b, a + b

print(res)