N = 600851475143
n = int(N ** 0.5) + 1


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    n -= 2
    if N % n == 0 and is_prime(n):
        break
print(n)
