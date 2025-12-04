import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    paper_coordinates = []
    for y, i in enumerate(lines):
        for x, j in enumerate(i):
            if j == "@":
                paper_coordinates.append((x, y))
    return paper_coordinates


def find_adjacent_rolls(roll, all_rolls):
    positions = [(roll[0], roll[1] - 1), (roll[0] + 1, roll[1] - 1), (roll[0] + 1, roll[1]), (roll[0] + 1, roll[1] + 1),
                 (roll[0], roll[1] + 1), (roll[0] - 1, roll[1] + 1), (roll[0] - 1, roll[1]), (roll[0] - 1, roll[1] - 1)]
    adjacent = len(set(all_rolls) & set(positions))
    return adjacent


start_time = time.time()
g1 = read_file('input_day4.txt')

answer = 0
for i in g1:
    answer += 1 if find_adjacent_rolls(i, g1) < 4 else 0

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()

answer2 = 0
answer_tmp = 1
while answer_tmp != 0:
    answer_tmp = 0
    g1_temp = g1.copy()
    for i in g1:
        tmp = find_adjacent_rolls(i, g1)
        answer_tmp += 1 if tmp < 4 else 0
        if tmp < 4:
            g1_temp.remove(i)
    g1 = g1_temp
    answer2 += answer_tmp

print('2nd part answer: ' + str(answer2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))