from tqdm import trange

all_numbers_dict = {}


def sort_n(n):
    n = str(n)
    n = [i for i in n]
    n = sorted(n)
    n = ''.join(n)
    return n


for i in trange(10_000):
    j = i
    i = i ** 3
    i = sort_n(i)
    if i in all_numbers_dict:
        all_numbers_dict[i]['amount'] += 1
        all_numbers_dict[i]['numbers'].append(j**3)
    else:
        all_numbers_dict[i] = {}
        all_numbers_dict[i]['amount'] = 1
        all_numbers_dict[i]['numbers'] = [j**3]

    if all_numbers_dict[i]['amount'] == 5:
        print(min(all_numbers_dict[i]['numbers']))
        break
