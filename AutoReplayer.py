import pygame
from engine import Engine
from Solution import Game
from Solution2 import Game2
import random


def winner(map_):
    for i in range(0, 3):
        if map_[i, 0] == map_[i, 1] == map_[i, 2] != -1 != 2:
            return map_[i, 0]
        if map_[0, i] == map_[1, i] == map_[2, i] != -1 != 2:
            return map_[0, i]
    if map_[0, 0] == map_[1, 1] == map_[2, 2] != -1 != 2:
        return map_[0, 0]
    if map_[2, 0] == map_[1, 1] == map_[0, 2] != -1 != 2:
        return map_[i, 0]
    return -1



def can_not(x, y, map_, common_map):
    if map_[y, x] != -1:
        return True
    elif common_map[y // 3, x // 3] != -1:
        return True
    else:
        return False


def is_leaf(map_):
    if winner(map_) != -1:
        return True
    for i in range(3):
        for j in range(3):
            if map_[i, j] == -1:
                return False
    return True


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
game = Game()
game2 = Game2()
engine = Engine()
score_1 = 0
score_2 = 0
win.fill((0, 0, 0))
pygame.display.update()
n = 1
while True:
    game = Game()
    engine = Engine()
    game2 = Game2()
    for i in range(n, 20 + n):
        x, y = round(random.uniform(0, 8)), round(random.uniform(0, 8))
        while can_not(x, y, engine.map_, engine.common_map):
            x, y = round(random.uniform(0, 8)), round(random.uniform(0, 8))
        if i % 2 == 0:
            pl = 1
        else:
            pl = 0
        game.map_[y, x] = pl
        game2.map_[y, x] = int(pl == 0)
        engine.map_[y, x] = pl
        for i in range(3):
            for j in range(3):
                min_map = game.map_[3 * i:3 * (i + 1), 3 * j:3 * (j + 1)]
                if is_leaf(min_map):
                    game.common_map[i, j] = winner(min_map)
        for i in range(3):
            for j in range(3):
                min_map = game2.map_[3 * i:3 * (i + 1), 3 * j:3 * (j + 1)]
                if is_leaf(min_map):
                    game2.common_map[i, j] = winner(min_map)
        for i in range(3):
            for j in range(3):
                min_map = engine.map_[3 * i:3 * (i + 1), 3 * j:3 * (j + 1)]
                if is_leaf(min_map):
                    engine.common_map[i, j] = winner(min_map)
    n = int(n == 0)
    if n == 0:
        info1 = list(engine.get_info())
        engine.play(*game.step(*info1))
        game.update_chances(engine.common_map, engine.map_)
    while not engine.is_leaf(engine.common_map):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        info1 = list(engine.get_info())
        engine.play(*game2.step(*info1))
        game2.update_chances(engine.common_map, engine.map_)
        draw_window(win, engine.map_, engine.common_map)
        if not engine.is_leaf(engine.common_map):
            info1 = list(engine.get_info())
            engine.play(*game.step(*info1))
            game.update_chances(engine.common_map, engine.map_)
            draw_window(win, engine.map_, engine.common_map)
    if engine.winner == 0:
        if n == 0:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('SOLUTION2', 250)
            textsurface = myfont.render('SOLUTION2', False, (255, 255, 255))
            win.blit(textsurface, (500, 400))
            score_1 += 1
        if n == 1:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('SOLUTION', 250)
            textsurface = myfont.render('SOLUTION', False, (255, 255, 255))
            win.blit(textsurface, (500, 400))
            score_2 += 1
    if engine.winner == 1:
        if n == 1:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('SOLUTION2', 250)
            textsurface = myfont.render('SOLUTION2', False, (255, 255, 255))
            win.blit(textsurface, (500, 400))
            score_1 += 1
        if n == 0:
            win.fill((0, 0, 0))
            myfont = pygame.font.SysFont('SOLUTION', 250)
            textsurface = myfont.render('SOLUTION', False, (255, 255, 255))
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