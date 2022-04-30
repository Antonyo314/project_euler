points = []

N = 50
for i in range(N + 1):
    for j in range(N + 1):
        points.append([i, j])

points = points[1:]


def length(point0, point1, point2):
    length0 = (point0[0] - point1[0]) ** 2 + (point0[1] - point1[1]) ** 2
    length1 = (point0[0] - point2[0]) ** 2 + (point0[1] - point2[1]) ** 2
    length2 = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    return [length0, length1, length2]


def right_angle(length):
    if length[0] + length[1] == length[2] or length[0] + length[2] == length[1] or length[1] + length[2] == length[0]:
        return True
    else:
        return False


point0 = 0, 0
result = 0
for i, point1 in enumerate(points):
    for point2 in points[i + 1:]:
        if right_angle(length(point0, point1, point2)):
            result += 1

print(result)
