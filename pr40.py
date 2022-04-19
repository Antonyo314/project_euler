arr = ''

it = 0
while len(arr) <= 1_000_000:
    arr += str(it)
    it += 1

result = 1
for i in [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]:
    result *= int(arr[i])
print(result)