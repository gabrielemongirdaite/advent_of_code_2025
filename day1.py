import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    instructions = []
    for i in lines:
        instructions.append((i[0], int(i[1:])))
    return instructions


start_time = time.time()
start_ind = 50
g1 = read_file('input_day1.txt')
zeros = 0
for i in g1:
    if i[0] == 'R':
        start_ind = (start_ind + i[1]) % 100
    else:
        start_ind = (start_ind - i[1]) % 100
    if start_ind == 0:
        zeros += 1
print('1st part answer: ' + str(zeros))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
passed_zeros = 0
zeros = 0
start_ind = 50
for i in g1:
    if i[0] == 'R':
        tmp = (start_ind + i[1])
        passed_zeros = abs(tmp // 100)
        start_ind = tmp % 100
    else:
        tmp = (start_ind - i[1])
        passed_zeros = abs(tmp // 100)
        if abs(tmp) == i[1]:
            passed_zeros = passed_zeros - 1 if passed_zeros > 0 else 0
        start_ind = tmp % 100
        if start_ind == 0:
            passed_zeros += 1
    zeros += passed_zeros

print('2nd part answer: ' + str(zeros))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
