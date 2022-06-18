def is_palindrome(s):
    s = str(s)
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


all_numbers = [i * j for i in range(999) for j in range(999)]
all_numbers = list(set(all_numbers))

all_numbers.sort(reverse=True)

for number in all_numbers:
    if is_palindrome(number):
        print(number)
        break
