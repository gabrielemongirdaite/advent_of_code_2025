import time
import re
import math


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lines_adj = []
    for i in lines[:-1]:
        i_tmp = re.findall(r'\d+', i)
        lines_adj.append(i_tmp)
    lines_adj.append(re.findall(r'\+|\*', lines[-1]))
    return lines, lines_adj


start_time = time.time()
g, g1 = read_file('input_day6.txt')
answer = 0

numbers = []
for i in range(0, len(g1[0])):
    tmp = []
    for j in g1[:-1]:
        tmp.append(int(j[i]))
    numbers.append(tmp)

for ind, i in enumerate(g1[-1]):
    if i == '+':
        answer += sum(numbers[ind])
    else:
        answer += math.prod(numbers[ind])

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
answer2 = 0
n = []
for i in range(0, len(g[0])):
    tmp = ''
    for j in g[:-1]:
        try:
            tmp += j[i]
        except:
            pass
    n.append(tmp)

ind = 0
a_tmp = 1
for i in n:
    if i == '    ':
        answer2 += a_tmp
        ind += 1
        if g1[-1][ind] == "+":
            a_tmp = 0
        else:
            a_tmp = 1
    else:
        if g1[-1][ind] == "+":
            a_tmp += int(i)
        else:
            a_tmp *= int(i)


answer2 += a_tmp
print('2nd part answer: ' + str(answer2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
