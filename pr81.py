import copy

f = open('p081_matrix.txt', 'r')
s = f.read()

arr = s.split('\n')

arr = arr[:-1]

arr = [[int(j) for j in a.split(',')] for a in arr]

# arr = [[131, 673, 234, 103, 18],
#        [201, 96, 342, 965, 150],
#        [630, 803, 746, 422, 111],
#        [537, 699, 497, 121, 956],
#        [805, 732, 524, 37, 331]]

arr_ = copy.deepcopy(arr)

for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        arr_[i][j] = 0

t = 0
for i in range(len(arr)):
    arr_[0][i] += t
    t = arr_[0][i]

t = 0
for i in range(len(arr)):
    arr_[i][0] += t
    t = arr_[i][0]

for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        arr_[i][j] = arr[i][j] + min(arr_[i - 1][j], arr_[i][j - 1])

n = len(arr_)

i, j = n - 1, n - 1
result = arr[i][j]

while i > 0 or j > 0:
    if i == 0:
        j -= 1
        result += arr[i][j]
    elif j == 0:
        i -= 1
        result += arr[i][j]
    else:
        if arr_[i - 1][j] < arr_[i][j - 1]:
            i -= 1
            result += arr[i][j]
        else:
            j -= 1
            result += arr[i][j]
print(result)
