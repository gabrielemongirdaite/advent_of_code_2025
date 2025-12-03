import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    joltage = []
    for i in lines:
        tmp = []
        for j in i:
            tmp.append(int(j))
        joltage.append(tmp)
    return joltage


def find_max(lst):
    mx = max(lst)
    ind = lst.index(mx)
    return mx, ind


start_time = time.time()
g1 = read_file('input_day3.txt')

answer = 0
for i in g1:
    mx1, ind1 = find_max(i[:-1])
    mx2, ind2 = find_max(i[ind1 + 1:])
    answer += mx1 * 10 + mx2

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
answer = 0
for i in g1:
    answer_tmp = 0
    ind = 0
    for k in range(11, -1, -1):
        if k == 0:
            mx1, ind1 = find_max(i[ind:])
        else:
            mx1, ind1 = find_max(i[ind:-k])
        ind += ind1 + 1
        answer_tmp += mx1 * 10 ** k
    answer += answer_tmp

print('2nd part answer: ' + str(answer))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
