import pygame
from engine import Engine
from Solution import Game


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
            pygame.draw.line(win, (255, 255, 255), (100+i*300, 0+j*300+10), (100+i*300, 300+j*300-10), 5)
            pygame.draw.line(win, (255, 255, 255), (200+i*300, 0+j*300+10), (200+i*300, 300+j*300-10), 5)
            pygame.draw.line(win, (255, 255, 255), (0+i*300+10, 100+j*300), (300+i*300-10, 100+j*300), 5)
            pygame.draw.line(win, (255, 255, 255), (0+i*30+10, 200+j*300), (300+i*300-10, 200+j*300), 5)
    if engine.ROW != -1:
        pygame.draw.line(win, (255, 0, 0), (engine.ROW*100, engine.COL*100), (engine.ROW*100+100, engine.COL*100), 5)
        pygame.draw.line(win, (255, 0, 0), (engine.ROW*100+100, engine.COL*100+100), (engine.ROW*100, engine.COL*100+100), 5)
        pygame.draw.line(win, (255, 0, 0), (engine.ROW*100+100, engine.COL*100), (engine.ROW*100+100, engine.COL*100+100), 5)
        pygame.draw.line(win, (255, 0, 0), (engine.ROW*100, engine.COL*100), (engine.ROW*100, engine.COL*100+100), 5)

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

    for i in range(3):
        for j in range(3):
            if common_map[i, j] != -1:
                pygame.draw.rect(win, (0, 0, 0), (j*300+6, i*300+6, 290, 290))
                if common_map[i, j] == 0:
                    pygame.draw.circle(win, (255, 0, 255), (j*300+150, i*300+150), 120, 9)
                else:
                    pygame.draw.line(win, (255, 0, 0), (j*300+30, i*300+30), (j*300+270, i*300+270), 9)
                    pygame.draw.line(win, (255, 0, 0), (j*300+270, i*300+30), (j*300+30, i*300+270), 9)
    if engine.ROW != -1 and common_map[engine.COL%3, engine.ROW%3] == -1:
        x = 300*(engine.ROW%3)+100
        y = 300*(engine.COL%3)
        pygame.draw.line(win, (0, 255, 0), (x, y+10), (x, y+300-10), 5)
        pygame.draw.line(win, (0, 255, 0), (x+100, y+10), (x+100, y+300-10), 5)
        pygame.draw.line(win, (0, 255, 0), (x-100+10, y+100), (x+200-10, y+100), 5)
        pygame.draw.line(win, (0, 255, 0), (x-100+10, y+200), (x+200-10, y+200), 5)

    pygame.display.update()


win = pygame.display.set_mode((900, 1000))

game = Game()
engine = Engine()

win.fill((0, 0, 0))
pygame.display.update()
n = 1

while True:
    game = Game()
    engine = Engine()
    n = int(n == 0)
    if n == 0:
        info1 = list(engine.get_info())
        engine.play(*game.step(*info1))
    while not is_leaf(engine.common_map):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = 3 * (engine.ROW % 3)
                y = 3 * (engine.COL % 3)
                if (engine.common_map[y//3, x//3] != -1) or (engine.ROW == -1) or ((x*100 < event.pos[0] < (x+3)*100) and (y*100 < event.pos[1] < (y+3)*100) and engine.map_[event.pos[1]//100, event.pos[0]//100] == -1):
                    engine.play(event.pos[0]//100, event.pos[1]//100)
                    info1 = list(engine.get_info())
                    engine.play(*game.step(*info1))

        draw_window(win, engine.map_, engine.common_map)