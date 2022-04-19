from tqdm import tqdm

f = open('/home/anton/PycharmProjects/project_euler/p042_words.txt', 'r')
s = f.read()

words = s.split(',')

words = [i[1:-1] for i in words]


def char2n(s):
    return ord(s) - 64


def word2n(word):
    res = 0
    for i in word:
        res += char2n(i)

    return res


word2n_dict = {}
for word in tqdm(words):
    word2n_dict[word] = word2n(word)

max_ = max(v for v in word2n_dict.values())

arr = []
n = 1
while True:
    t = n * (n + 1) / 2
    arr.append(int(t))

    if t > max_:
        break
    n += 1

result = 0
for v in word2n_dict.values():
    if v in arr:
        result += 1

print(result)
