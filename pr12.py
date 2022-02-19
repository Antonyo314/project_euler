def number_of_divisors(n):
    res = 0
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            res += 1
    return res * 2


i = 1
while True:
    print(i)
    i += 1
    if number_of_divisors(i * (i + 1) / 2) > 500:
        print(i * (i + 1) / 2)
        break
