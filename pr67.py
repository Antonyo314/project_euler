f = open('p067_triangle.txt', 'r')
s = f.read()

ar = s.split('\n')
arr = [[int(j) for j in i.split(' ')] for i in ar[:-1]]

for i in range(len(arr) - 1, 0, -1):
    for j in range(len(arr[i - 1])):
        arr[i - 1][j] = max(arr[i][j] + arr[i - 1][j], arr[i][j + 1] + arr[i - 1][j])

print(arr[0][0])
