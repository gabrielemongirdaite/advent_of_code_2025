import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    ind = max(loc for loc, val in enumerate(lines) if val == '')
    areas = []
    for i in lines[ind + 1:]:
        i1, i2 = i.split(": ")
        x, y = i1.split('x')
        i3 = i2.split(" ")
        areas.append([(int(x), int(y)), [int(k) for k in i3]])
    return areas


start_time = time.time()
g1 = read_file('input_day12.txt')
answer = 0

for ind, i in enumerate(g1):
    i12 = min(i[1][1], i[1][2])
    i1 = i[1][1] - i12 if i[1][1] > i[1][2] else 0
    i2 = i[1][2] - i12 if i[1][2] > i[1][1] else 0
    i5 = i[1][2] if i[1][2] < i[1][5] else i[1][5]
    i5_r = 0 if i[1][2] > i[1][5] else i[1][5] - i[1][2]
    if i[0][0] * i[0][1] - sum(i[1]) * 9 > 0:
        answer += 1
    elif i[0][0] * i[0][1] - i12 * 12 - i5 * 6 - (i[1][0] + i1 + i2 + i[1][3] + i[1][4] + i5_r) * 9 > 0:
        answer += 1


print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

# 994 -- too high
