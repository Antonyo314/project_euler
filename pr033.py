def f(a, b):
    if str(a)[-1] == '0' or str(b)[-1] == '0':
        return False
    s_a = set(str(a))
    s_b = set(str(b))
    if len(s_a.intersection(s_b)) > 0:
        t = list(s_a.intersection(s_b))[0]

        if len(t) > 0:
            s_a.remove(t)
            s_b.remove(t)
            if len(s_a) == 0 or len(s_b) == 0:
                return False
            s_a = int(''.join(list(s_a)))
            s_b = int(''.join(list(s_b)))
        if a / b == s_a / s_b:
            return True
        else:
            return False
    else:
        return False


fractions = []
for i in range(11, 100):
    for j in range(i + 1, 100):
        if f(i, j):
            print(f'{i}/{j}')
            fractions.append([i, j])

numerator = 1
denominator = 1
for f in fractions:
    numerator *= f[0]
    denominator *= f[1]

print(f'numerator: {numerator}')
print(f'denominator: {denominator}')
#100