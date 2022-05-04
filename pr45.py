N = 100_000
triangles = [int(n*(n+1)/2) for n in range(N)]
pentagonals = [int(n*(3*n-1)/2) for n in range(N)]
hexagonals = [int(n*(2*n-1)) for n in range(N)]

res = [i for i in set(triangles).intersection(pentagonals).intersection(hexagonals)]
res.sort()
res = [i for i in res if i >40755]
print(res[0])