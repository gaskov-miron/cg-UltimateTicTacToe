import numpy as np
import random

random.seed(100000)


class Game:
    def __init__(self):
        self.map_ = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

    def step(self, opponent_row, opponent_col, list_of_action):
        self.map_[opponent_col, opponent_row] = 0
        n = round(random.uniform(0, len(list_of_action)) - 1)
        row, col = list_of_action[n][0], list_of_action[n][1]
        self.map_[col, row] = 1
        return row, col


if __name__ == '__main__':
    game = Game()
    while True:
        opponent_row, opponent_col = map(int, input().split())
        validActionCount = int(input())
        list_of_action = [([int(j) for j in input().split()])for i in range(validActionCount)]
        row, col = game.step(opponent_row, opponent_col, list_of_action)
        print(str(row)+' '+str(col))