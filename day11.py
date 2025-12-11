import time
import copy


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    d = {}
    for i in lines:
        i_tmp = i.split(": ")
        tmp = i_tmp[1].split(" ")
        d[i_tmp[0]] = tmp
    return d


start_time = time.time()
g1 = read_file('input_day11.txt')
answer = 0
all_paths_tmp = [['you']]
while all_paths_tmp:
    paths_tmp = []
    for i in all_paths_tmp:
        last = i[-1]
        tmp = []
        try:
            for k in g1[last]:
                t = copy.deepcopy(i)
                t.append(k)
                tmp.append(t)
        except:
            pass
        if tmp:
            paths_tmp.extend(tmp)
    all_paths_tmp = paths_tmp
    if all_paths_tmp:
        answer = len(all_paths_tmp)

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
all_paths_tmp = {('svr', 0, 0): 1}  # dac fft all
a2 = 0
while all_paths_tmp:
    paths_tmp = {}
    for i in all_paths_tmp:
        tmp = {}
        dac = i[1]
        fft = i[2]
        try:
            for k in g1[i[0]]:
                if k == 'dac':
                    tmp[(k, 1, fft)] = all_paths_tmp[i]
                elif k == 'fft':
                    tmp[(k, dac, 1)] = all_paths_tmp[i]
                else:
                    tmp[(k, dac, fft)] = all_paths_tmp[i]
        except:
            pass
        if tmp:
            for i in tmp:
                if i in paths_tmp:
                    paths_tmp[i] += tmp[i]
                else:
                    paths_tmp[i] = tmp[i]
    all_paths_tmp = paths_tmp
    if ('out', 1, 1) in all_paths_tmp:
        a2 += all_paths_tmp[('out', 1, 1)]

print('2nd part answer: ' + str(a2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
