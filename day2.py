import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split(',')
    id_ranges = []
    for i in lines:
        i1, i2 = i.split("-")
        id_ranges.append(range(int(i1), int(i2) + 1))
    return id_ranges


def if_invalid(r):
    r_str = str(r)
    if len(r_str) % 2 == 1:
        return 0
    else:
        mid = len(r_str) // 2
        if r_str[0:mid] == r_str[mid:]:
            return r
        else:
            return 0


def if_valid_part_2(r):
    r_str = str(r)
    if len(r_str) == 1:
        return 0
    else:
        for i in range(1, len(r_str)):
            if len(r_str) % i != 0:
                pass
            else:
                parts = [r_str[k:k + i] for k in range(0, len(r_str), i)]
                if len(parts) > 1 and len(set(parts)) == 1:
                    return r
    return 0


def find_invalid_in_range(r, part=1):
    all = 0
    for i in r:
        if part == 1:
            all += if_invalid(i)
        else:
            tmp = if_valid_part_2(i)
            all += tmp
    return all


start_time = time.time()
g1 = read_file('input_day2.txt')
answer = 0
for j in g1:
    answer += find_invalid_in_range(j)

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
answer = 0
for j in g1:
    answer += find_invalid_in_range(j, 2)

print('2nd part answer: ' + str(answer))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
