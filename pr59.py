from tqdm import trange

f = open('p059_cipher.txt', 'r')
s = f.read()

arr = s.split(',')


def solution():
    for a in trange(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                res = []
                for a_, b_, c_ in zip(arr[::3], arr[1::3], arr[2::3]):
                    res.extend([chr(a ^ int(a_)), chr(b ^ int(b_)), chr(c ^ int(c_))])

                res = ''.join(res)
                if "Euler's" in res:
                    print(res)
                    print(sum(ord(i) for i in res))
                    return


solution()
