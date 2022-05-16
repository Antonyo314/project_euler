import copy
from pprint import pprint
import numpy as np

f = open('p082_matrix.txt', 'r')
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

for i in range(0, len(arr)):
    for j in range(1, len(arr)):
        arr_[i][j] = 10 ** 10


for i in range(1, len(arr_)):
    converged = False
    while not converged:
        converged = True
        for j in range(len(arr_)):
            old_value = arr_[j][i]
            if j == 0:
                arr_[j][i] = min(arr_[j][i - 1], arr_[j + 1][i]) + arr[j][i]
            elif j == len(arr_) - 1:
                arr_[j][i] = min(arr_[j][i - 1], arr_[j - 1][i]) + arr[j][i]
            else:
                arr_[j][i] = min(arr_[j][i - 1], arr_[j + 1][i], arr_[j - 1][i]) + arr[j][i]
            if old_value != arr_[j][i]:
                converged = False


j = np.argmin([arr_[j][-1] for j in range(len(arr_))])
i = len(arr_) - 1
result = arr[j][i]

while i > 0:
    if j == 0:
        if arr_[j][i - 1] < arr_[j + 1][i]:
            i -= 1
        else:
            j += 1
    elif j == len(arr_) - 1:
        if arr_[j][i - 1] < arr_[j - 1][i]:
            i -= 1
        else:
            j -= 1
    elif arr_[j][i - 1] < arr_[j + 1][i] and arr_[j][i - 1] < arr_[j - 1][i]:
        i -= 1
    elif arr_[j + 1][i] < arr_[j][i - 1] and arr_[j + 1][i] < arr_[j - 1][i]:
        j += 1
    else:
        j -= 1
    result += arr[j][i]

print(result)
