import numpy as np


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

    def play(self, row, col):
        self.ROW, self.COL = row, col
        self.map_[col, row] = self.CurrentPlayer
        self.CurrentPlayer = int(self.CurrentPlayer == 0)

    def get_info(self):
        x = 3*(self.ROW % 3)
        y = 3*(self.COL % 3)
        list_of_actions = []
        for i in range(x, x+3):
            for j in range(y, y+3):
                if self.map_[j, i] == -1:
                    list_of_actions.append((i, j))
        return self.ROW, self.COL, list_of_actions