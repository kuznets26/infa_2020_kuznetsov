import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 100
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
                                  (int(x - 200 * font_size1), int(y - 60 * font_size1))])
    inscription_font = pygame.font.SysFont('Arial Black', font_size)
    inscription1 = inscription_font.render("Smashed it: " + str(s), 5, (255, 50, 100))
    inscription = inscription_font.render("Missed: " + str(k), 5, (255, 50, 100))  # inscription
    screen.blit(inscription1, (x, y))  # where to
    screen.blit(inscription, (x, y + 20 * font_size1))

balls_q = 8
A = [0] * balls_q
for i in range(balls_q):
    A[i] = [0, 0, 0, 0, 0, 0]
print(A)


def ball(n):
    global A
    A[n][0] = randint(100, 700)
    A[n][1] = randint(100, 500)
    A[n][2] = randint(30, 50)
    A[n][3] = COLORS[randint(0, 5)]
    A[n][4] = randint(5, 50)
    A[n][5] = randint(5, 50)
    circle(screen, A[n][3], (A[n][0], A[n][1]), A[n][2])



while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)
    score(900, 600, 22)
    for i in range(balls_q):
            ball(i)
            A[i][0] += 5
            A[i][1] += 6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(balls_q):
                if (event.pos[0] - A[i][0]) ** 2 + (event.pos[1] - A[i][1]) ** 2 < r ** 2:
                    s += 1
                    screen.fill(BLACK)
                    score(900, 600, 22)
                    ball(i)
                    pygame.display.update()
                else:
                    k += 1
                    screen.fill(BLACK)
                    score(900, 600, 22)
                    ball(i)
                    pygame.display.update()


    screen.fill(BLACK)


pygame.quit()