import copy
from pprint import pprint

f = open('p083_matrix.txt', 'r')
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

for i in range(len(arr)):
    for j in range(len(arr)):
        arr_[i][j] = 10 ** 10

arr_[0][0] = arr[0][0]


converged = False
while not converged:
    converged = True
    for j in range(len(arr_)):
        for i in range(len(arr_)):
            old_value = arr_[j][i]
            if j == i == 0:
                pass
            elif j == 0 and i == len(arr_) - 1:
                arr_[j][i] = min(arr_[j + 1][i], arr_[j][i - 1]) + arr[j][i]
            elif j == len(arr_) - 1 and i == 0:
                arr_[j][i] = min(arr_[j - 1][i], arr_[j][i + 1]) + arr[j][i]
            elif j == len(arr_) - 1 and i == len(arr_) - 1:
                arr_[j][i] = min(arr_[j - 1][i], arr_[j][i - 1]) + arr[j][i]
            elif i == 0:
                arr_[j][i] = min(arr_[j - 1][i], arr_[j][i + 1], arr_[j + 1][i + 1],
                                 arr_[j + 1][i]) + arr[j][i]
            elif i == len(arr_) - 1:
                arr_[j][i] = min(arr_[j - 1][i], arr_[j][i - 1],
                                 arr_[j + 1][i]) + arr[j][i]
            elif j == 0:
                arr_[j][i] = min(arr_[j][i - 1], arr_[j + 1][i],
                                 arr_[j][i + 1]) + arr[j][i]
            elif j == len(arr_) - 1:
                arr_[j][i] = min(arr_[j][i - 1], arr_[j - 1][i],
                                 arr_[j][i + 1]) + arr[j][i]

            else:
                arr_[j][i] = min(arr_[j - 1][i], arr_[j][i - 1], arr_[j][i + 1],
                                 arr_[j + 1][i]) + arr[j][i]

            if old_value != arr_[j][i]:
                converged = False

pprint(arr_[-1][-1])
