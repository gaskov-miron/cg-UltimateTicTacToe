import numpy as np
dic = {}


def get_map_(index):
    map_ = np.array([[ -1,  -1,  -1],
                     [ -1,  -1,  -1],
                     [ -1,  -1,  -1]])
    b = ''
    while index > 0:
        b = b+str(index % 3)
        index = index // 3
    b = b+(9-len(b))*'0'
    for i in range(3):
        for j in range(3):
            map_[j, i] = int(b[j+i*3]) - 1

    return map_


def get_index(map_):
    k = 0
    num = 0
    for i in range(3):
        for j in range(3):
            num += (map_[j, i]+1)*(3**k)
            k += 1
    return num


def winner(map_):
    for i in range(0, 3):
        if map_[i, 0] == map_[i, 1] == map_[i, 2] != -1:
            return map_[i, 0]
        if map_[0, i] == map_[1, i] == map_[2, i] != -1:
            return map_[0, i]
    if map_[0, 0] == map_[1, 1] == map_[2, 2] != -1:
        return map_[0, 0]
    if map_[2, 0] == map_[1, 1] == map_[0, 2] != -1:
        return map_[i, 0]
    return -1


def is_leaf(map_):
    if winner(map_) != -1:
        return True
    for i in range(3):
        for j in range(3):
            if map_[i, j] == -1:
                return False
    return True


def get_chance(map_):
    map_id = get_index(map_)
    if map_id in dic:
        return dic[map_id]
    if is_leaf(map_):
        if winner(map_) == 1:
            result = 1
        elif winner(map_) == 0:
            result = -1
        else:
            result = 0
    else:
        max_chance = -1
        min_chance = 1
        for i in range(3):
            for j in range(3):

                if map_[j, i] == -1:
                    map_[j, i] = 1
                    chance = get_chance(map_)
                    if chance > max_chance:
                        max_chance = chance
                    map_[j, i] = 0
                    chance = get_chance(map_)
                    if chance < min_chance:
                        min_chance = chance
                    map_[j, i] = -1

        result = 0.5*max_chance+0.5*min_chance
    dic[map_id] = result
    return result

map_ = np.array([[-1, -1, -1],
                 [-1, -1, -1],
                 [-1, -1, -1]])
t = ''
for i in range(19682):
    t += '|'+str(get_chance(get_map_(i)))
print(t[1:])
z = 0