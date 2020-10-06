import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1000
screen = pygame.display.set_mode((1200, 900))
screen.fill((0, 0, 0))


# defining some colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# drawing a ball with random colors
def new_ball():
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click():
    print(x, y, r, s)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

s = 0
k = 0


# drawing score table
def score(x, y, font_size):
    font_size1 = font_size // 22
    polygon(screen, (255, 0, 255), [(int(x - 200 * font_size1), int(y + 60 * font_size1)),
                                  (int(x + 200 * font_size1), int(y + 60 * font_size1)),
                                  (int(x + 200 * font_size1), int(y - 60 * font_size1)),
                                  (int(x - 400 * font_size1), int(y - 60 * font_size1))])
    inscription_font = pygame.font.SysFont('Arial Black', font_size)
    inscription1 = inscription_font.render("Smashed it: " + str(s), 5, (255, 50, 100))
    inscription = inscription_font.render("Missed: " + str(k), 5, (255, 50, 100))  # inscription
    screen.blit(inscription1, (x, y))  # where to
    screen.blit(inscription, (x, y + 20 * font_size1))


new_ball()
pygame.display.update()
start_time = pygame.time.get_ticks()
while not finished:
    clock.tick(FPS)
    if pygame.time.get_ticks() - start_time > 1000:
        k += 1
        screen.fill(BLACK)
        score(800, 600, 22)
        new_ball()
        pygame.display.update()
        start_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 < r ** 2:
                s += 1
                screen.fill(BLACK)
                score(800, 600, 22)
                new_ball()
                pygame.display.update()
                start_time = pygame.time.get_ticks()
            else:
                k += 1
                screen.fill(BLACK)
                score(800, 600, 22)
                new_ball()
                pygame.display.update()
                start_time = pygame.time.get_ticks()


    screen.fill(BLACK)


pygame.quit()