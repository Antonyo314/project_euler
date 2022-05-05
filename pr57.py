def f():
    a, b = 3, 2
    while True:
        yield a, b
        a, b = a + b + b, a + b


gen = f()

result = 0
for i in range(1_000):
    a, b = next(gen)
    if len(str(a)) > len(str(b)):
        result += 1

print(result)
