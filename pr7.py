# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
N = 200_000

prime_dict = {}

for i in range(2, N):
    prime_dict[i] = True

for i in range(2, N):
    if prime_dict[i]:
        for j in range(2 * i, N, i):
            prime_dict[j] = False


amount = 0
for i in range(2, N):
    if prime_dict[i]:
        amount += 1
    if amount == 10_001:
        print(i)
        break
