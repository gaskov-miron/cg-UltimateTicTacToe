import numpy as np


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


class Engine:
    def __init__(self):
        self.ROW = -1
        self.COL = -1
        self.CurrentPlayer = 1
        self.common_map = np.array([[-1, -1, -1],
                                    [-1, -1, -1],
                                    [-1, -1, -1]])

        self.map_ = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

    def play(self, row, col):
        self.ROW, self.COL = row, col
        if self.map_[col, row] == -1:
            self.map_[col, row] = self.CurrentPlayer
        else:
            print(row, col, self.map_[col, row])
            raise()
        self.CurrentPlayer = int(self.CurrentPlayer == 0)
        for i in range(3):
            for j in range(3):
                min_map = self.map_[3*j:3*(j+1), 3*i:3*(i+1)]
                if is_leaf(min_map):
                    self.common_map[j, i] = winner(min_map)

    def get_info(self):
        x = 3*(self.ROW % 3)
        y = 3*(self.COL % 3)
        list_of_actions = []
        if self.common_map[y//3, x//3] == -1:
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if self.map_[j, i] == -1:
                        list_of_actions.append((i, j))
        else:
            for i in range(9):
                for j in range(9):
                    if self.map_[j, i] == -1:
                        list_of_actions.append((i, j))

        return self.ROW, self.COL, list_of_actions