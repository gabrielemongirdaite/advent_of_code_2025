import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def splitter_coords(manifold):
    splitters = []
    for y, i in enumerate(manifold):
        for x, j in enumerate(i):
            if j == 'S':
                start_point = (x, y)
            elif j == '^':
                splitters.append((x, y))
    return start_point, splitters


def beam_move(start_point, splitters, manifold):
    split = 0
    max_y = len(manifold)
    beams = [start_point]
    while beams:
        beams_tmp = []
        for i in beams:
            if i[1] + 1 == max_y:
                break
            elif manifold[i[1] + 1][i[0]] == '.':
                beams_tmp.append((i[0], i[1] + 1))
            elif (i[0], i[1] + 1) in splitters:
                beams_tmp.extend([(i[0] - 1, i[1] + 1), (i[0] + 1, i[1] + 1)])
                split += 1
        beams = list(set(beams_tmp))
    return split


def beam_move_part2(start_point, splitters, manifold):
    split = 0
    max_y = len(manifold)
    beams = {start_point: 1}
    while beams:
        beams_tmp = {}
        for i in beams:
            if i[1] + 1 == max_y:
                break
            elif manifold[i[1] + 1][i[0]] == '.':
                if (i[0], i[1] + 1) in beams_tmp:
                    beams_tmp[(i[0], i[1] + 1)] += beams[i]
                else:
                    beams_tmp[(i[0], i[1] + 1)] = beams[i]
            elif (i[0], i[1] + 1) in splitters:
                if (i[0] - 1, i[1] + 1) in beams_tmp:
                    beams_tmp[(i[0] - 1, i[1] + 1)] += beams[i]
                else:
                    beams_tmp[(i[0] - 1, i[1] + 1)] = beams[i]

                if (i[0] + 1, i[1] + 1) in beams_tmp:
                    beams_tmp[(i[0] + 1, i[1] + 1)] += beams[i]
                else:
                    beams_tmp[(i[0] + 1, i[1] + 1)] = beams[i]
        split = sum(beams.values())
        beams = beams_tmp
    return split


start_time = time.time()
g1 = read_file('input_day7.txt')
start_point, splitters = splitter_coords(g1)
answer = beam_move(start_point, splitters, g1)

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
answer2 = beam_move_part2(start_point, splitters, g1)

print('2nd part answer: ' + str(answer2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
