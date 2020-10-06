import pygame
import math as m
from pygame.draw import *
from random import randint

pygame.init()

FPS = 160
width_screen = 800
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen))
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


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# counting hits and misses
hit = 0
miss = 0

# text lifetime
text_lifetime = 1000
text_start_ticks = 0
text_options = ['SMASHED IT!!!', 'GOOD JOB, LAD!', 'NICE, BRO!']
text = ''


def draw_inscription():
    time = pygame.time.get_ticks()
    global text
    global width_screen
    global height_screen
    global text_start_ticks
    global text_lifetime
    if text_start_ticks + text_lifetime > time:
        inscription_font = pygame.font.SysFont('Arial Black', 80)
        size = inscription_font.size(text)
        inscription = inscription_font.render(text, 5, COLORS[randint(0, 5)])
        screen.blit(inscription, ((width_screen - size[0]) // 2, height_screen // 3))


def create_inscription():
    global text
    global text_start_ticks
    text = text_options[randint(0, 2)]
    text_start_ticks = pygame.time.get_ticks()


# drawing score table
def score(x, y, font_size):
    font_size1 = font_size // 22
    polygon(screen, (0, 0, 200), [(int(x - width_screen // 4 * font_size1), int(y + height_screen // 12 * font_size1)),
                                    (int(x + width_screen // 4 * font_size1), int(y + height_screen // 12 * font_size1)),
                                    (int(x + width_screen // 4 * font_size1), int(y - height_screen // 12 * font_size1)),
                                    (int(x - width_screen // 4 * font_size1), int(y - height_screen // 12 * font_size1))])
    inscription_font = pygame.font.SysFont('Arial Black', font_size)
    inscription1 = inscription_font.render("Hit: " + str(hit), 5, (255, 50, 100))
    inscription = inscription_font.render("Missed: " + str(miss), 5, (255, 50, 100))  # inscription
    screen.blit(inscription1, (x, y))  # where to
    screen.blit(inscription, (x, y + 20 * font_size1))


balls_q = 10
Ball_Parameters = [0] * balls_q
for i in range(balls_q):
    Ball_Parameters[i] = [0, 0, 0, 0, 0, 0]


def create_ball(n):
    global Ball_Parameters
    Ball_Parameters[n][0] = randint(100, 700)  # x
    Ball_Parameters[n][1] = randint(100, 500)  # y
    Ball_Parameters[n][2] = randint(30, 50)  # radius
    Ball_Parameters[n][3] = COLORS[randint(0, 5)]  # colors
    Ball_Parameters[n][4] = randint(-500, 500)  # vx
    Ball_Parameters[n][5] = randint(-500, 500)  # vy


def draw_ball(n):
    global Ball_Parameters
    circle(screen, Ball_Parameters[n][3], (round(Ball_Parameters[n][0]),
                                           round(Ball_Parameters[n][1])), Ball_Parameters[n][2])


# makes the world fly
def move_ball(n):
    global Ball_Parameters
    Ball_Parameters[n][0] += Ball_Parameters[n][4] / FPS
    Ball_Parameters[n][1] += Ball_Parameters[n][5] / FPS
    if Ball_Parameters[n][0] - Ball_Parameters[n][2] < 0:
        Ball_Parameters[n][4] = - Ball_Parameters[n][4]
    if Ball_Parameters[n][1] - Ball_Parameters[n][2] < 0:
        Ball_Parameters[n][5] = - Ball_Parameters[n][5]
    if Ball_Parameters[n][0] + Ball_Parameters[n][2] > width_screen:
        Ball_Parameters[n][4] = - Ball_Parameters[n][4]
    if Ball_Parameters[n][1] + Ball_Parameters[n][2] > height_screen:
        Ball_Parameters[n][5] = - Ball_Parameters[n][5]


def ball_handle_event_hit(event, i):
    global hit
    global Ball_Parameters
    if (event.pos[0] - Ball_Parameters[i][0]) ** 2 + \
            (event.pos[1] - Ball_Parameters[i][1]) ** 2 < Ball_Parameters[i][2] ** 2:
        hit += 1
        create_ball(i)
        return True
    return False

shape_q = 3
Shape_Parameters = [0] * shape_q
for i in range(shape_q):
    Shape_Parameters[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def create_shape(n):
    global Shape_Parameters
    Shape_Parameters[n][0] = randint(100, 700)  # x
    Shape_Parameters[n][1] = randint(100, 500)  # y
    Shape_Parameters[n][2] = randint(30, 50)  # radius
    Shape_Parameters[n][3] = COLORS[randint(0, 5)]  # colors
    Shape_Parameters[n][4] = randint(-500, 500)  # vx
    Shape_Parameters[n][5] = randint(-500, 500)  # vy
    Shape_Parameters[n][6] = randint(3, 9)  # quantity of angles
    Shape_Parameters[n][7] = randint(0, round(2 * m.pi))  # rotation angle
    Shape_Parameters[n][8] = randint(0, round(5 * m.pi))  # OMEGA motherfucker do you speak it???


def draw_shape(n):
    global Shape_Parameters
    shape_vertices = [0] * Shape_Parameters[n][6]
    alpha = 2 * m.pi / Shape_Parameters[n][6]
    for i in range(Shape_Parameters[n][6]):
        shape_vertices[i] = (round(Shape_Parameters[n][0] + Shape_Parameters[n][2] * m.cos(Shape_Parameters[n][7] + alpha * i)),
                             round(Shape_Parameters[n][1] + Shape_Parameters[n][2] * m.sin(Shape_Parameters[n][7] + alpha * i)))
    polygon(screen, Shape_Parameters[n][3], shape_vertices)


# makes the world fly
def move_shape(n):
    global Shape_Parameters
    Shape_Parameters[n][0] += Shape_Parameters[n][4] / FPS
    Shape_Parameters[n][1] += Shape_Parameters[n][5] / FPS
    Shape_Parameters[n][7] += Shape_Parameters[n][8] / FPS
    if Shape_Parameters[n][0] - Shape_Parameters[n][2] < 0:
        Shape_Parameters[n][4] = - Shape_Parameters[n][4]
    if Shape_Parameters[n][1] - Shape_Parameters[n][2] < 0:
        Shape_Parameters[n][5] = - Shape_Parameters[n][5]
    if Shape_Parameters[n][0] + Shape_Parameters[n][2] > width_screen:
        Shape_Parameters[n][4] = - Shape_Parameters[n][4]
    if Shape_Parameters[n][1] + Shape_Parameters[n][2] > height_screen:
        Shape_Parameters[n][5] = - Shape_Parameters[n][5]


def shape_handle_event_hit(event, i):
    global hit
    global Shape_Parameters
    alpha = 2 * m.pi / Shape_Parameters[i][6]
    f = True
    for j in range(Shape_Parameters[i][6]):
        a_x = Shape_Parameters[i][0] + Shape_Parameters[i][2] * m.cos(Shape_Parameters[i][7] + alpha * j)
        a_y = Shape_Parameters[i][1] + Shape_Parameters[i][2] * m.sin(Shape_Parameters[i][7] + alpha * j)
        b_x = Shape_Parameters[i][0] + Shape_Parameters[i][2] * m.cos(Shape_Parameters[i][7] + alpha * (j + 1))
        b_y = Shape_Parameters[i][1] + Shape_Parameters[i][2] * m.sin(Shape_Parameters[i][7] + alpha * (j + 1))
        ev_point_x = event.pos[0] - a_x
        ev_point_y = event.pos[1] - a_y
        v_x = b_x - a_x
        v_y = b_y - a_y
        det = - ev_point_x * v_y + ev_point_y * v_x
        if det < 0:
            f = False
            break
    if f:
        hit += 5
        create_inscription()
        create_shape(i)
        return True
    return False


for i in range(balls_q):
    create_ball(i)
for i in range(shape_q):
    create_shape(i)
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bool_event = False
            for i in range(balls_q):
                bool_event = ball_handle_event_hit(event, i) or bool_event
            for i in range(shape_q):
                bool_event = shape_handle_event_hit(event, i) or bool_event
            if not bool_event:
                miss += 1
    screen.fill(BLACK)
    score(500, 500, 22)
    draw_inscription()
    for i in range(balls_q):
        move_ball(i)
        draw_ball(i)
    for i in range(shape_q):
        move_shape(i)
        draw_shape(i)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()