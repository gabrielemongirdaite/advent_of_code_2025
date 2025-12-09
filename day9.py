import time
import itertools
from matplotlib import pyplot as plt


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    l = []
    for i in lines:
        i1, i2 = i.split(',')
        l.append((int(i1), int(i2)))
    return l


def find_distances(all_coords):
    comb = itertools.combinations(all_coords, 2)
    max_area = 0
    for i in comb:
        x = abs(i[0][0] - i[1][0]) + 1
        y = abs(i[0][1] - i[1][1]) + 1
        area = x * y
        if max_area < area:
            max_area = area
    return max_area


def add_perimeter_green(red):
    green_red = []
    for ind, curr in enumerate(red):
        if curr == red[-1]:
            ind = -1
        nxt = red[ind + 1]
        green_red.append(curr)
        if curr[0] == nxt[0]:
            for i in range(min(curr[1], nxt[1]) + 1, max(curr[1], nxt[1])):
                green_red.append((curr[0], i))
        else:
            for i in range(min(curr[0], nxt[0]) + 1, max(curr[0], nxt[0])):
                green_red.append((i, curr[1]))
        green_red.append(nxt)
    return green_red[:-1]


def find_distances_part2(f, s, t, fo, t_all, fo_all):
    comb1 = itertools.product(f, t)
    comb2 = itertools.product(s, fo)
    max_area = 0
    for i in comb1:
        c1 = (i[0][0], i[1][1])
        all_relevant_tmp = []
        for i1 in t_all:
            if i1[0] == c1[0] and i1[1] != c1[1]:
                all_relevant_tmp.append(i1[1])
        if all_relevant_tmp:
            if c1[1] <= min(all_relevant_tmp):
                x = abs(i[0][0] - i[1][0]) + 1
                y = abs(i[0][1] - i[1][1]) + 1
                area = x * y
                if max_area < area:
                    max_area = area
    for i in comb2:
        c1 = (i[0][0], i[1][1])
        all_relevant_tmp = []
        for i1 in fo_all:
            if i1[0] == c1[0] and i1[1] != c1[1]:
                all_relevant_tmp.append(i1[1])
        if all_relevant_tmp:
            if c1[1] >= max(all_relevant_tmp):
                x = abs(i[0][0] - i[1][0]) + 1
                y = abs(i[0][1] - i[1][1]) + 1
                area = x * y
                if max_area < area:
                    max_area = area
    return max_area


start_time = time.time()
g1 = read_file('input_day9.txt')
answer = find_distances(g1)

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
red_green_tiles = add_perimeter_green(g1)

# plt.scatter(*zip(*red_green_tiles))
# plt.show()

first = [i for i in g1 if i[1] == 50137]
second = [i for i in g1 if i[1] == 48623]
third = [i for i in g1 if i[1] > 50137]
fourth = [i for i in g1 if i[1] < 48623]

third_all = [i for i in red_green_tiles if i[1] > 50137]
fourth_all = [i for i in red_green_tiles if i[1] < 48623]

answer2 = find_distances_part2(first, second, third, fourth, third_all, fourth_all)

print('2nd part answer: ' + str(answer2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
