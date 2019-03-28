from Solution import Game
from engine import Engine
e = Engine()
g = Game()
x = e.get_info()[2]
print(x)
print(g.step(8, 5, x))