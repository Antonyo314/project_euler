def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = a + b, a


def number_len(n):
    return len(str(n))


fib_generator = fib()

it = 1
while True:
    x = next(fib_generator)
    it += 1
    if number_len(x) == 1_000:
        print(it)
        break
