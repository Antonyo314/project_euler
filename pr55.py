def is_palindrome(x):
    s = str(x)
    n = len(s)
    if n % 2 == 0:
        for i in range(int(n / 2)):
            if s[i] != s[-(i + 1)]:
                return False
        return True
    else:
        for i in range(int((n - 1) / 2)):
            if s[i] != s[-(i + 1)]:
                return False
        return True


def is_lychrel(n, it=0):
    if is_palindrome(n) and 0 < it < 50:
        return False
    elif it > 50:
        return True
    else:
        it += 1
        return is_lychrel(n + int(str(n)[::-1]), it)


res = 0
for i in range(1, 10_000+1):
    if is_lychrel(i):
        res += 1
print(res)
