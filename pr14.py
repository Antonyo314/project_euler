def len_chain(n):
    res = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        res += 1
    return res + 1


maximum = 0
result = 0
for i in range(1, 1_000_000):
    len_ = len_chain(i)
    if len_ > maximum:
        maximum = len_
        result = i
print(result)
