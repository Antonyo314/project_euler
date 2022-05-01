def eratosphene(n):
    arr = list(range(n + 1))
    arr[1] = 0

    for i in range(2, len(arr)):
        for j in range(i * 2, len(arr), i):
            arr[j] = 0
    arr = [i for i in arr if i != 0]
    return arr


primes = eratosphene(1_000_000)

for n in range(7037, 100_000, 2):
    if n * 2 * primes[n - 1] > 10 ** 10:
        print(n)
        break
