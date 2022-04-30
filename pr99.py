import math

math.log(math.e)
f = open('/home/anton/PycharmProjects/project_euler/p099_base_exp.txt', 'r')
s = f.read()

arr = s.split('\n')

arr = [[int(j) for j in i.split(',')] for i in arr]


def f(a, n):
    return n * math.log(a)


d = {}

for i, a in enumerate(arr):
    d[i] = f(a[0], a[1])

print(max(d, key=d.get) + 1)
