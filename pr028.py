j = 2
a = 1
# print(a)
N = 1001
n = int((N - 1)/2)
res = a
for i in range(n):
    for _ in range(4):
        a += j
        res += a
        # print(a)
    j += 2

print(res)
