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


class Engine:
    def __init__(self):
        self.ROW = -1
        self.COL = -1
        self.CurrentPlayer = 1
        self.map_ = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

        self.common_map = np.array([[-1, -1, -1],
                                    [-1, -1, -1],
                                    [-1, -1, -1]])
        self.winner = None

    def play(self, row, col):
        if self.is_leaf(self.common_map) is False:
            self.ROW, self.COL = row, col
            if self.map_[row, col] == -1:
                self.map_[row, col] = self.CurrentPlayer
            else:
                print(row, col, self.common_map[row // 3, col // 3])
                raise()
            self.CurrentPlayer = int(self.CurrentPlayer == 0)
            for i in range(3):
                for j in range(3):
                    min_map = self.map_[3*i:3*(i+1), 3*j:3*(j+1)]
                    if self.is_leaf(min_map):
                        self.common_map[i, j] = winner(min_map)
        else:
            self.winner = winner(self.common_map)

    def is_leaf(self, map_):
        if winner(map_) != -1:
            return True
        for i in range(3):
            for j in range(3):
                if map_[i, j] == -1:
                    return False
        return True

    def get_info(self):
        x = 3*(self.COL % 3)
        y = 3*(self.ROW % 3)
        list_of_actions = []
        if self.common_map[y//3, x//3] == -1 and self.COL != -1:
            for i in range(y, y+3):
                for j in range(x, x+3):
                    if self.map_[i, j] == -1:
                        list_of_actions.append((i, j))
        else:
            for i in range(9):
                for j in range(9):
                    if self.map_[i, j] == -1 and self.common_map[i // 3, j // 3] == -1:
                        list_of_actions.append((i, j))

        return self.ROW, self.COL, list_of_actions