arr = []
for i in range(1, 100):
    for j in range(1, 100):
        arr.append(i ** j)

arr = list(set(arr))


def digits_sum(n):
    arr = [int(i) for i in str(n)]
    return sum(arr)


res_arr = []
for i in arr:
    res_arr.append(digits_sum(i))

print(max(res_arr))
