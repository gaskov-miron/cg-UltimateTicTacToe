import pygame
import numpy as np
from solution import score
from solution import is_leaf


def draw_window(win, map_, score_1, score_2):

    pygame.draw.line(win, (255, 255, 255), (300, 0), (300, 900), 1)
    pygame.draw.line(win, (255, 255, 255), (600, 0), (600, 900), 1)
    pygame.draw.line(win, (255, 255, 255), (0, 300), (900, 300), 1)
    pygame.draw.line(win, (255, 255, 255), (0, 600), (900, 600), 1)

    pygame.draw.line(win, (255, 255, 255), (0, 900), (900, 900), 1)
    pygame.draw.line(win, (255, 255, 255), (0, 0), (900, 0), 1)
    pygame.draw.line(win, (255, 255, 255), (0, 0), (0, 900), 1)
    pygame.draw.line(win, (255, 255, 255), (899, 0), (899, 900), 1)

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('SCORE '+str(score_1)+' : '+str(score_2), False, (255, 255, 255))
    win.blit(textsurface, (400, 920))

    for i in range(3):
        for j in range(3):
            if map_[i, j] == 0:
                pygame.draw.circle(win, (0, 0, 255), (j*300+150, i*300+150), 100, 3)
            elif map_[i, j] == 1:
                pygame.draw.line(win, (255, 0, 0), (j*300+15, i*300+15), (j*300+285, i*300+285), 3)
                pygame.draw.line(win, (255, 0, 0), (j*300+285, i*300+15), (j*300+15, i*300+285), 3)
    pygame.display.update()


win = pygame.display.set_mode((900, 1000))

player = 0

score_1 = 0
score_2 = 0

while True:
    player = int(player == 0)
    map_ = np.array([[-1,  -1,  -1],
                     [-1,  -1,  -1],
                     [-1,  -1,  -1]])
    win.fill((0, 0, 0))
    pygame.display.update()

    if player == 0:
        state, pos = score(map_, int(player == 0))
        map_[pos[0], pos[1]] = int(player == 0)
    while is_leaf(map_) == 0:
        draw_window(win, map_, score_1, score_2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0] // 300
                y = event.pos[1] // 300
                if map_[y, x] == -1:
                    map_[y, x] = player
                    state, pos = score(map_, int(player == 0))
                    if pos is not None:
                        map_[pos[0], pos[1]] = int(player == 0)

    draw_window(win, map_, score_1, score_2)

    for i in range(0, 3):
        if map_[0, i] == map_[1, i] == map_[2, i] != -1:
            pygame.draw.line(win, (255, 255, 0), (i*300+150, 15), (i*300+150, 885), 3)
            if map_[0, i] == player:
                score_1 += 1
            else:
                score_2 += 1
        if map_[i, 0] == map_[i, 1] == map_[i, 2] != -1:
            pygame.draw.line(win, (255, 255, 0), (15, i*300+150), (885, i*300+150), 3)
            if map_[i, 0] == player:
                score_1 += 1
            else:
                score_2 += 1
    if map_[0, 0] == map_[1, 1] == map_[2, 2] != -1:
        pygame.draw.line(win, (255, 255, 0), (15, 15), (885, 885), 3)
        if map_[0, 0] == player:
            score_1 += 1
        else:
            score_2 += 1
    if map_[2, 0] == map_[1, 1] == map_[0, 2] != -1:
        pygame.draw.line(win, (255, 255, 0), (885, 15), (15, 885), 3)
        if map_[2, 0] == player:
            score_1 += 1
        else:
            score_2 += 1

    pygame.display.update()

    pygame.time.delay(3000)