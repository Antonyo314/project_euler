from tqdm import trange


def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def is_pandigital(n):
    n = str(n)
    arr = [i for i in n]
    if len(set(arr)) != len(arr):
        return False

    for i in range(1, len(n) + 1):
        if str(i) not in arr:
            return False
    return True


#987654321 % 3 == 0 because 9+8+7+6+5+4+3+2+1 = 45%3==0 the same for all 9-digit pandigital numbers
#the same for 87654321 and all 8-digit pandigital numbers
#that's why we starts from 7654321

for i in trange(7654321, 0, -2):
    if is_pandigital(i) and is_prime(i):
        print(i)
        break
