prime_dict = {}

for i in range(2, 2_000_000):
    prime_dict[i] = True

for i in prime_dict.keys():
    if prime_dict[i]:
        for j in range(2 * i, 2_000_000, i):
            prime_dict[j] = False

res = 0
for i in range(2, 2_000_000):
    if prime_dict[i]:
        res += i

print(res)
