import pygame
import numpy as np
from engine import Engine
from Solution import Game


def draw_window(win, map_):
    win.fill((0, 0, 0))

    for i in range(3):
        for j in range(3):
            pygame.draw.line(win, (255, 255, 255), (100+i*300, 0+j*300), (100+i*300, 300+j*300), 5)
            pygame.draw.line(win, (255, 255, 255), (200+i*300, 0+j*300), (200+i*300, 300+j*300), 5)
            pygame.draw.line(win, (255, 255, 255), (0+i*300, 100+j*300), (300+i*300, 100+j*300), 5)
            pygame.draw.line(win, (255, 255, 255), (0+i*300, 200+j*300), (300+i*300, 200+j*300), 5)

    pygame.draw.line(win, (255, 200, 0), (300, 0), (300, 900), 10)
    pygame.draw.line(win, (255, 200, 0), (600, 0), (600, 900), 10)
    pygame.draw.line(win, (255, 200, 0), (0, 300), (900, 300), 10)
    pygame.draw.line(win, (255, 200, 0), (0, 600), (900, 600), 10)

    for i in range(9):
        for j in range(9):
            if map_[i, j] == 0:
                pygame.draw.circle(win, (255, 0, 255), (j*100+50, i*100+50), 40, 3)
            elif map_[i, j] == 1:
                pygame.draw.line(win, (255, 0, 0), (j*100+10, i*100+10), (j*100+90, i*100+90), 3)
                pygame.draw.line(win, (255, 0, 0), (j*100+90, i*100+10), (j*100+10, i*100+90), 3)
    pygame.display.update()


win = pygame.display.set_mode((900, 1000))

game1 = Game()
game2 = Game()
engine = Engine()

n = 0

win.fill((0, 0, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if n == 0:
                    info1 = list(engine.get_info())
                    engine.play(*game1.step(*info1))
                else:
                    info2 = list(engine.get_info())
                    engine.play(*game2.step(*info2))
                n = int(n == 0)

    draw_window(win, engine.map_)