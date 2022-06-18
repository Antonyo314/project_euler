res = 0
for n in range(1, 100):
    for j in range(1, 20):
        t = str(j ** n)

        if len(t) == n:
            res += 1
        elif len(t) > n:
            break

print(res)
