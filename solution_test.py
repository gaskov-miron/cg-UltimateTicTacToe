import numpy as np
import copy
import random
from Solution import *

map_ = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

common_map = np.array([[-1, -1, -1],
                       [-1, -1, -1],
                       [-1, -1, -1]])

X_chances, O_chances = get_Xchances_Ochances(map_)


print(X_chances, '\n', O_chances)
Xw, Ow, N = get_common_chances(common_map, X_chances, O_chances)
print(Xw, Ow, N)
print(Xw - Ow)