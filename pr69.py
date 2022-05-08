def eratosphene(n):
    arr = list(range(n + 1))
    arr[1] = 0

    for i in range(2, len(arr)):
        for j in range(i * 2, len(arr), i):
            arr[j] = 0
    arr = [i for i in arr if i != 0]
    return arr


primes = eratosphene(1_000_000)

result = 1
it = 0
while result <= 10 ** 6:
    result *= primes[it]
    it += 1

if result > 10 ** 6:
    result /= primes[it - 1]
print(int(result))
