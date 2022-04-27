f = open('p102_triangles.txt', 'r')
s = f.read()

arr = s.split('\n')

arr = [[int(j) for j in i.split(',')] for i in arr[:-1]]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def build_line(A, B):
    x0 = A.x
    y0 = A.y
    x1 = B.x
    y1 = B.y
    if x1 == x0:
        k = 0
    else:
        k = (y1 - y0) / (x1 - x0)
    b = y0 - k * x0
    return k, b


def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1


def traingle_contain_origin(A, B, C):
    ab_k, ab_b = build_line(A, B)
    bc_k, bc_b = build_line(B, C)
    ac_k, ac_b = build_line(A, C)

    if sign(-ab_b) != sign(C.y - ab_k * C.x - ab_b) and ab_b != 0 and C.y - ab_k * C.x - ab_b != 0:
        return False
    elif sign(-bc_b) != sign(A.y - bc_k * A.x - bc_b) and bc_b != 0 and A.y - bc_k * A.x - bc_b != 0:
        return False
    elif sign(-ac_b) != sign(B.y - ac_k * B.x - ac_b) and ac_b != 0 and B.y - ac_k * B.x + ac_b != 0:
        return False
    else:
        return True


result = 0
for a in arr:
    A = Point(a[0], a[1])
    B = Point(a[2], a[3])
    C = Point(a[4], a[5])

    if traingle_contain_origin(A, B, C):
        result += 1

print(result)
