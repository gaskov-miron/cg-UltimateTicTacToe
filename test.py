from Solution import Game
from engine import Engine
import numpy as np
import copy
e = Engine()
g = Game()
x = e.get_info()[2]
MAP_ = np.array([[-1, 1, 1],
                       [-1, -1, -1],
                       [-1, -1, -1]])
MAP_D = np.array([[-1, 0, 0],
                       [-1, -1, -1],
                       [-1, -1, -1]])

for i in range(4):
    print(MAP_)
    MAP_ = copy.deepcopy(np.rot90(MAP_))
    print(MAP_D)
    MAP_D = copy.deepcopy(np.rot90(MAP_D))
MAP_ = copy.deepcopy(np.flip(MAP_, 0))
MAP_D = copy.deepcopy(np.flip(MAP_D, 0))
for i in range(4):
    print(MAP_)
    MAP_ = copy.deepcopy(np.rot90(MAP_))
    print(MAP_D)
    MAP_D = copy.deepcopy(np.rot90(MAP_D))