from tqdm import trange, tqdm

s = open('p098_words.txt', 'r').read()
arr = s.split(',')

arr = [i[1:-1] for i in arr]

max_ = max([len(i) for i in arr])


def squares_of_len(n):
    a = int('1' + '0' * (n - 1))

    if int(a ** 0.5) == a ** 0.5:
        a = int(a ** 0.5)
    else:
        a = int(a ** 0.5) + 1

    b = int('9' * n)
    if int(b ** 0.5) == b ** 0.5:
        b = int(b ** 0.5)
    else:
        b = int(b ** 0.5)
    squares = [i ** 2 for i in range(a, b + 1)]
    return squares


def anagrams(a, b):
    d1, d2 = dict(), dict()

    for i in a:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in b:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1

    if d1 == d2:
        return True
    else:
        return False


len2squares = dict()

for i in range(2, 15):
    len2squares[i] = squares_of_len(i)

max_ = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if anagrams(arr[i], arr[j]):

            squares = squares_of_len(len(arr[i]))

            for square in squares:
                square_string = str(square)
                temp_d = dict()

                is_possible_to_replace = True
                for x, y in zip(arr[i], square_string):
                    if x not in temp_d:
                        temp_d[x] = y
                    elif temp_d[x] != y:
                        is_possible_to_replace = False
                        break

                if not is_possible_to_replace or len(set(temp_d.keys())) != len(set(temp_d.values())):
                    continue

                second_number = int(''.join([str(temp_d[i]) for i in arr[j]]))
                if second_number in squares:
                    if second_number > max_:
                        max_ = second_number
                    elif square > max_:
                        max_ = square

print(max_)
