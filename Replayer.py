import pygame
from engine import Engine
from Solution2 import Game2
import numpy as np


def draw_window(win, map_, common_map):
    win.fill((0, 0, 0))
    for i in range(3):
        for j in range(3):
            pygame.draw.line(win, (255, 255, 255), (100+j*300, 0+i*300+10), (100+j*300, 300+i*300-10), 5)
            pygame.draw.line(win, (255, 255, 255), (200+j*300, 0+i*300+10), (200+j*300, 300+i*300-10), 5)
            pygame.draw.line(win, (255, 255, 255), (0+j*300+10, 100+i*300), (300+j*300-10, 100+i*300), 5)
            pygame.draw.line(win, (255, 255, 255), (0+j*30+10, 200+i*300), (300+j*300-10, 200+i*300), 5)
    if engine.ROW != -1:
        pygame.draw.line(win, (255, 0, 0), (engine.COL*100, engine.ROW*100), (engine.COL*100+100, engine.ROW*100), 5)
        pygame.draw.line(win, (255, 0, 0), (engine.COL*100+100, engine.ROW*100+100), (engine.COL*100, engine.ROW*100+100), 5)
        pygame.draw.line(win, (255, 0, 0), (engine.COL*100+100, engine.ROW*100), (engine.COL*100+100, engine.ROW*100+100), 5)
        pygame.draw.line(win, (255, 0, 0), (engine.COL*100, engine.ROW*100), (engine.COL*100, engine.ROW*100+100), 5)

    pygame.draw.line(win, (255, 200, 0), (300, 0), (300, 900), 10)
    pygame.draw.line(win, (255, 200, 0), (600, 0), (600, 900), 10)
    pygame.draw.line(win, (255, 200, 0), (0, 300), (900, 300), 10)
    pygame.draw.line(win, (255, 200, 0), (0, 600), (900, 600), 10)

    pygame.draw.line(win, (255, 200, 0), (1200, 150), (1200, 750), 10)
    pygame.draw.line(win, (255, 200, 0), (1400, 150), (1400, 750), 10)
    pygame.draw.line(win, (255, 200, 0), (1000, 350), (1600, 350), 10)
    pygame.draw.line(win, (255, 200, 0), (1000, 550), (1600, 550), 10)

    for i in range(3):
        for j in range(3):
            ID = game.get_index(engine.map_[i*3:(i+1)*3, j*3:(j+1)*3])
            Pw = game.chances[ID][0]
            Pl = game.chances[ID][1]

            pygame.font.init()
            myfont = pygame.font.SysFont('Comic Sans MS', 20)

            textsurface = myfont.render(str(Pw), False, (255, 255, 255))
            win.blit(textsurface, (1050+j*200, 200+i*200))

            textsurface = myfont.render(str(Pl), False, (255, 255, 255))
            win.blit(textsurface, (1050+j*200, 225+i*200))

    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = myfont.render(str(game.Xw)+' '+str(game.Ow)+' '+str(game.N), False, (255, 255, 255))
    win.blit(textsurface, (1000, 50))
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('score_you: ' + str(score_1), False, (255, 255, 255))
    win.blit(textsurface, (1000, 800))
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('score_bot: ' + str(score_2), False, (255, 255, 255))
    win.blit(textsurface, (1000, 850))

    for i in range(9):
        for j in range(9):
            if map_[i, j] == 0:
                pygame.draw.circle(win, (255, 0, 255), (j*100+50, i*100+50), 40, 3)
            elif map_[i, j] == 1:
                pygame.draw.line(win, (255, 0, 0), (j*100+10, i*100+10), (j*100+90, i*100+90), 3)
                pygame.draw.line(win, (255, 0, 0), (j*100+90, i*100+10), (j*100+10, i*100+90), 3)

    for i in range(3):
        for j in range(3):
            if common_map[i, j] != -1:
                pygame.draw.rect(win, (0, 0, 0), (j*300+6, i*300+6, 290, 290))
                if common_map[i, j] == 0:
                    pygame.draw.circle(win, (255, 0, 255), (j*300+150, i*300+150), 120, 9)
                else:
                    pygame.draw.line(win, (255, 0, 0), (j*300+30, i*300+30), (j*300+270, i*300+270), 9)
                    pygame.draw.line(win, (255, 0, 0), (j*300+270, i*300+30), (j*300+30, i*300+270), 9)
    if engine.ROW != -1 and common_map[engine.ROW%3, engine.COL%3] == -1:
        x = 300*(engine.COL%3)+100
        y = 300*(engine.ROW%3)
        pygame.draw.line(win, (0, 255, 0), (x, y+10), (x, y+300-10), 5)
        pygame.draw.line(win, (0, 255, 0), (x+100, y+10), (x+100, y+300-10), 5)
        pygame.draw.line(win, (0, 255, 0), (x-100+10, y+100), (x+200-10, y+100), 5)
        pygame.draw.line(win, (0, 255, 0), (x-100+10, y+200), (x+200-10, y+200), 5)
    pygame.display.update()


win = pygame.display.set_mode((1700, 900))
game = Game2()
engine = Engine()
score_1 = 0
score_2 = 0
win.fill((0, 0, 0))
pygame.display.update()
n = 1
while True:
    game = Game2()
    engine = Engine()
    n = int(n == 0)
    if n == 0:
        info1 = list(engine.get_info())
        row, col = game.step(*info1)
        engine.play(row, col)
        game.update_chances(engine.common_map, engine.map_)
    while not engine.is_leaf(engine.common_map):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = 3 * (engine.COL % 3)
                y = 3 * (engine.ROW % 3)
                if (engine.common_map[y//3, x//3] != -1) or (engine.ROW == -1) or ((x*100 < event.pos[0] < (x+3)*100) and (y*100 < event.pos[1] < (y+3)*100) and engine.map_[event.pos[1]//100, event.pos[0]//100] == -1):
                    engine.play(event.pos[1]//100, event.pos[0]//100)
                    info1 = list(engine.get_info())
                    row, col = game.step(*info1)
                    engine.play(row, col)
                    game.update_chances(engine.common_map, engine.map_)
        draw_window(win, engine.map_, engine.common_map)
    if engine.winner == 0:
        if n == 0:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('YOU WIN', 250)
            textsurface = myfont.render('YOU WIN', False, (255, 255, 255))
            win.blit(textsurface, (500, 400))
            score_1 += 1
        if n == 1:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('YOU LOSE', 250)
            textsurface = myfont.render('YOU LOSE', False, (255, 255, 255))
            win.blit(textsurface, (500, 400))
            score_2 += 1
    if engine.winner == 1:
        if n == 1:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('YOU WIN', 250)
            textsurface = myfont.render('YOU WIN', False, (255, 255, 255))
            win.blit(textsurface, (500, 400))
            score_1 += 1
        if n == 0:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('YOU LOSE', 250)
            textsurface = myfont.render('YOU LOSE', False, (255, 255, 255))
            win.blit(textsurface, (500, 400))
            score_2 += 1
    if engine.winner == -1:
        win.fill((0, 0, 0))
        myfont = pygame.font.SysFont('NOBODY LOSE, NOBODY WIN', 50)
        textsurface = myfont.render('NOBODY LOSE, NOBODY WIN', False, (255, 255, 255))
        win.blit(textsurface, (400, 400))
    game.update_chances(engine.common_map, engine.map_)
    pygame.display.update()
    pygame.time.delay(5000)