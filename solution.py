import numpy as np


ME = 1
steps = 0


def draw_window(map_):
    for i in range(3):
        t = ''
        for j in range(3):
            t += (' ', '0', 'X')[map_[i, j]+1]+'|'
        print(t[:-1])
        if i != 2:
            print('-+-+-')
            
            
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


def score(map_, player):
    global steps
    #if steps > 10:
    #    return
    #steps += 1

    if is_leaf(map_):
        if winner(map_) == -1:
            return 0, None
        elif winner(map_) == ME:
            return 1, None
        else:
            return -1, None
    else:
        best_step, best_score = None, None
        for i in range(3):
            for j in range(3):
                if map_[i, j] == -1:
                    map_[i, j] = player
                    num = [-1, 1][int(player == ME)]
                    new_score = score(map_, int(player == 0))[0]
                    if new_score == num:
                        map_[i, j] = -1
                        return num, (i, j)
                    if best_score is None or new_score > best_score and player == ME:
                        best_step, best_score = (i, j), new_score
                    if best_score is None or new_score < best_score and player != ME:
                        best_step, best_score = (i, j), new_score
                    map_[i, j] = -1
        return best_score, best_step


map_ = np.array([[ 1,  1,  0],
                 [ 0,  0,  1],
                 [ 1,  1,  0]])
draw_window(map_)
print(score(map_, 1))
