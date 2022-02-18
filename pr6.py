N = 100
a = sum([i**2 for i in range(1, N+1)])
b = sum([i for i in range(1, N+1)])**2
print(b-a)