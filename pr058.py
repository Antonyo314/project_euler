def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


it = 1
all = 1
prime_numbers = 0
for i in range(2, 100_000, 2):
    for j in range(4):
        it += i
        all += 1
        if is_prime(it):
            prime_numbers += 1
    if prime_numbers / all <= 0.1:
        print(i + 1)
        break
