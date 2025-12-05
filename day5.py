import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    ind = lines.index('')
    ranges = []
    indexes = []
    for i in lines[0:ind]:
        i1, i2 = i.split("-")
        ranges.append((int(i1), int(i2)))
    for j in lines[ind + 1:]:
        indexes.append(int(j))
    return ranges, indexes


def is_fresh(ind, ranges):
    for i in ranges:
        if i[0] <= ind <= i[1]:
            return 1
    return 0


start_time = time.time()
g1, g2 = read_file('input_day5.txt')
answer = 0

for i in g2:
    answer += is_fresh(i, g1)
print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
answer2 = 0
g_new = []
while g1:
    i = g1[0]
    within = 0
    if len(g_new) == 0:
        answer2 += i[1] - i[0] + 1
    else:
        i_tmp = i
        for j in g_new:
            if i[1] <= j[1] and i[0] >= j[0]:
                within = 1
            elif i_tmp[1] >= j[1] >= i_tmp[0] >= j[0]:
                i_tmp = (j[1] + 1, i_tmp[1])
            elif j[1] >= i_tmp[1] >= j[0] >= i_tmp[0]:
                i_tmp = (i_tmp[0], j[0] - 1)
            elif i_tmp[1] >= j[1] and i_tmp[0] <= j[0]:
                within = 1
                g1.extend([(i_tmp[0], j[0] - 1), (j[1] + 1, i_tmp[1])])
        answer2 += i_tmp[1] - i_tmp[0] + 1 if within == 0 else 0
    g1.pop(0)
    if within == 0:
        g_new.append(i)

print('2nd part answer: ' + str(answer2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

