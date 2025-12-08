import math
import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    l = []
    for i in lines:
        i1, i2, i3 = i.split(',')
        l.append([(int(i1), int(i2), int(i3))])
    return l


def calculate_all_distances(coords):
    all_pairs = [(x[0], y[0]) for x in coords for y in coords if x != y]
    all_pairs_adj = []
    for i in all_pairs:
        dist = math.sqrt((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2 + (i[0][2] - i[1][2]) ** 2)
        all_pairs_adj.append([i, dist])
    return all_pairs_adj


def join_boxes(box_1, box_2, circuits):
    for ind, i in enumerate(circuits):
        if box_1 in i:
            ind1 = ind
        if box_2 in i:
            ind2 = ind
    if ind2 != ind1:
        circuits[ind2].extend(circuits[ind1])
        circuits.pop(ind1)
    return circuits


def find_minimum_distance(all_distances):
    min_distance = 10000000
    for i in all_distances:
        if i[1] < min_distance:
            min_distance = i[1]
            a = i
    all_distances.remove(a)
    all_distances.remove([(a[0][1], a[0][0]), a[1]])
    return a, all_distances


start_time = time.time()
g1 = read_file('input_day8.txt')
all_distances = calculate_all_distances(g1)

for i in range(0, 1000):
    a, all_distances = find_minimum_distance(all_distances)
    g1 = join_boxes(a[0][0], a[0][1], g1)

l = []
for i in g1:
    l.append(len(i))

l = list(set(l))
l.sort(reverse=True)

print('1st part answer: ' + str(l[0] * l[1] * l[2]))
print("--- %s seconds for 1st part---" % (time.time() - start_time))  # 54s

start_time = time.time()

while len(g1) > 2:
    a, all_distances = find_minimum_distance(all_distances)
    g1 = join_boxes(a[0][0], a[0][1], g1)

min_distance = 10000000
for i1 in g1[0]:
    for i2 in g1[1]:
        tmp = math.sqrt((i1[0] - i2[0]) ** 2 + (i1[1] - i2[1]) ** 2 + (i1[2] - i2[2]) ** 2)
        if tmp < min_distance:
            a_tmp = (i1, i2)
            a1 = i1[0] * i2[0]
            min_distance = tmp

print('2nd part answer: ' + str(a1))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))  # 249s
