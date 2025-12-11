import time
import copy
from sympy import *
import itertools


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lights = []
    buttons_tmp = []
    joltage_tmp = []
    buttons = []
    joltage = []
    for i in lines:
        i_tmp = i.split(' ')
        lights.append(i_tmp[0][1:-1])
        joltage_tmp.append(i_tmp[-1][1:-1])
        buttons_tmp.append(i_tmp[1:-1])
    for i in buttons_tmp:
        tmp_1 = []
        for j in i:
            tmp = j[1:-1].split(',')
            tmp = [int(x) for x in tmp]
            tmp_1.append(tmp)
        buttons.append(tmp_1)
    for i in joltage_tmp:
        tmp = i.split(',')
        tmp = [int(x) for x in tmp]
        joltage.append(tmp)
    return lights, buttons, joltage


def find_mismatches(target_lights, current_lights):
    mismatches = []
    for ind, i in enumerate(target_lights):
        if i != current_lights[ind]:
            mismatches.append(ind)
    return mismatches


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


def new_lights(current_lights, buttons):
    for i in buttons:
        newstring = '.' if current_lights[i] == '#' else '#'
        current_lights = replacer(current_lights, newstring, i)
    return current_lights


def find_all_button_combinations(target_lights, buttons):
    start_lights = ['.' * len(target_lights)]
    lights_states = [start_lights[0]]
    presses = []
    pressed_buttons = []
    f = 0
    while start_lights:
        start_lights_tmp = []
        pressed_buttons_tmp = []
        for ind, s in enumerate(start_lights):
            mismatches = find_mismatches(target_lights, s)
            for i in buttons:
                for k in mismatches:
                    if k in i:
                        if f == 0:
                            tmp = [i]
                            pressed_buttons_tmp.append(tmp)
                        else:
                            tmp = copy.deepcopy(pressed_buttons[ind])
                            tmp.append(i)
                            pressed_buttons_tmp.append(tmp)
                        nl = new_lights(s, i)
                        if nl == target_lights:
                            presses.append(len(tmp))
                            pressed_buttons_tmp.remove(tmp)
                        elif nl not in lights_states:
                            lights_states.append(nl)
                            start_lights_tmp.append(nl)
        pressed_buttons = pressed_buttons_tmp
        start_lights = start_lights_tmp
        f += 1
    return presses


def create_equation(button, joltage):
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = symbols(
        ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12'])
    max_x = max(list(itertools.chain(*button)))
    equations = []
    xs = []
    if len(button) == 1:
        eq_0 = x0
        xs = [x0]
    elif len(button) == 2:
        eq_0 = x0 + x1
        xs = [x0, x1]
    elif len(button) == 3:
        eq_0 = x0 + x1 + x2
        xs = [x0, x1, x2]
    elif len(button) == 4:
        eq_0 = x0 + x1 + x2 + x3
        xs = [x0, x1, x2, x3]
    elif len(button) == 5:
        eq_0 = x0 + x1 + x2 + x3 + x4
        xs = [x0, x1, x2, x3, x4]
    elif len(button) == 6:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5
        xs = [x0, x1, x2, x3, x4, x5]
    elif len(button) == 7:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5 + x6
        xs = [x0, x1, x2, x3, x4, x5, x6]
    elif len(button) == 8:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7
        xs = [x0, x1, x2, x3, x4, x5, x6, x7]
    elif len(button) == 9:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8
        xs = [x0, x1, x2, x3, x4, x5, x6, x7, x8]
    elif len(button) == 10:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
        xs = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]
    elif len(button) == 11:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10
        xs = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
    elif len(button) == 12:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11
        xs = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]
    elif len(button) == 13:
        eq_0 = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12
        xs = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]
    else:
        print('mistake')
    for k in range(0, max_x + 1):
        tmp_eq = 0
        for indx, b in enumerate(button):
            if k in b:
                if indx == 0:
                    x = x0
                elif indx == 1:
                    x = x1
                elif indx == 2:
                    x = x2
                elif indx == 3:
                    x = x3
                elif indx == 4:
                    x = x4
                elif indx == 5:
                    x = x5
                elif indx == 6:
                    x = x6
                elif indx == 7:
                    x = x7
                elif indx == 8:
                    x = x8
                elif indx == 9:
                    x = x9
                elif indx == 10:
                    x = x10
                elif indx == 11:
                    x = x11
                elif indx == 12:
                    x = x12
                else:
                    print('mistake')
                tmp_eq += x
        tmp_eq -= joltage[k]
        equations.append(tmp_eq)
    for n in range(0, 100):
        equations_tmp = copy.deepcopy(equations)
        eq_0_tmp = copy.deepcopy(eq_0)
        t = max(joltage) + n
        eq_0_tmp -= t
        equations_tmp.append(eq_0_tmp)
        equations_tmp.append(x11-12)
        equations_tmp.append(x12)
        sol = solve(equations_tmp, xs)
        print(t, sol)
    return


start_time = time.time()
lights, buttons, joltage = read_file('input_day10.txt')

answer = 0
for i in range(0, len(lights)):
    answer += min(find_all_button_combinations(lights[i], buttons[i]))

print('1st part answer: ' + str(answer))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


ind = 122
create_equation(buttons[ind], joltage[ind])
# manually looked through each equation and found answers
