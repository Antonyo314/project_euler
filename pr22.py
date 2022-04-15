def char_number(char):
    return ord(char) - 64


def name2value(name):
    res = 0
    for char in name:
        res += char_number(char)

    return res


f = open('p022_names.txt', 'r')
s = f.read()

names = s.split(',')

names = [name[1:-1] for name in names]

names = sorted(names)
result = 0
for it, name in enumerate(names):
    result += (it + 1) * name2value(name)
print(result)
