def good(x):
    if set(str(x)) == set(str(x * 2)) == set(str(x * 3)) == set(str(x * 4)) == set(str(x * 5)) == set(str(x * 6)):
        return True
    else:
        return False


for i in range(1, 1_000_000):
    if good(i):
        print(i)
        break
