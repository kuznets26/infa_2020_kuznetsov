import pygame
import math as m
from pygame.draw import *
from random import randint

pygame.init()

# defining dimensions of a screen
FPS = 500
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
COLORS = [GREEN, BLUE, MAGENTA, CYAN, YELLOW, RED]


def ball_change_color(n):
    Ball_Parameters[n][3] = COLORS[(Ball_Parameters[n][2] - Rmin) // ((Rmax - Rmin)//len(COLORS))-1]


def shape_change_color(n):
    Shape_Parameters[n][3] = COLORS[(Shape_Parameters[n][2] - Rmin) // ((Rmax - Rmin)//len(COLORS))-1]


"""
x, y - position of the ball
r - radius of the ball
"""

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


# drawing inscription(look at text_options)
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


# particularly creates inscription
def create_inscription():
    global text
    global text_start_ticks
    text = text_options[randint(0, 2)]
    text_start_ticks = pygame.time.get_ticks()


# drawing score table
def score(x, y, font_size):
    polygon(screen, (0, 0, 200), [(int(x - 5.5 * font_size), int(y + 2.3 * font_size)),
                                  (int(x + 5.5 * font_size), int(y + 2.3 * font_size)),
                                  (int(x + 5.5 * font_size), int(y - 2.3 * font_size)),
                                  (int(x - 5.5 * font_size), int(y - 2.3 * font_size))])
    inscription_font = pygame.font.SysFont('Arial Black', font_size)
    inscription1 = inscription_font.render("Hit: " + str(hit), 5, (255, 50, 100))
    inscription = inscription_font.render("Missed: " + str(miss), 5, (255, 50, 100))  # inscription
    screen.blit(inscription1, (x, y))  # where to
    screen.blit(inscription, (x, y + font_size))


Rmax = 100
Rmin = 30
# number of balls
balls_q = 5
Ball_Parameters = [0] * balls_q
for i in range(balls_q):
    Ball_Parameters[i] = [0] * 7


# creates a ball and contains its parameters
def create_ball(n):
    global Ball_Parameters
    Ball_Parameters[n][0] = randint(100, 700)  # x
    Ball_Parameters[n][1] = randint(100, 500)  # y
    Ball_Parameters[n][2] = randint(Rmin, (Rmax + 3 * Rmin) // 4)  # radius
    ball_change_color(n)  # colors
    Ball_Parameters[n][4] = randint(80, 500) * (randint(0, 1) * 2 - 1)  # vx - speed xlabel
    Ball_Parameters[n][5] = randint(80, 500) * (randint(0, 1) * 2 - 1)  # vy - speed ylabel
    Ball_Parameters[n][6] = pygame.time.get_ticks()


# draws a ball
def draw_ball(n):
    global Ball_Parameters
    circle(screen, Ball_Parameters[n][3], (round(Ball_Parameters[n][0]),
                                           round(Ball_Parameters[n][1])), Ball_Parameters[n][2])


# makes the world fly(moves balls from place to place using parameters of a ball)
def move_ball(n):
    global Ball_Parameters
    Ball_Parameters[n][0] += Ball_Parameters[n][4] / FPS
    Ball_Parameters[n][1] += Ball_Parameters[n][5] / FPS
    if Ball_Parameters[n][0] - Ball_Parameters[n][2] < 0:
        Ball_Parameters[n][4] = - Ball_Parameters[n][4]
        Ball_Parameters[n][0] += Ball_Parameters[n][4] / FPS
    if Ball_Parameters[n][1] - Ball_Parameters[n][2] < 0:
        Ball_Parameters[n][5] = - Ball_Parameters[n][5]
        Ball_Parameters[n][1] += Ball_Parameters[n][5] / FPS
    if Ball_Parameters[n][0] + Ball_Parameters[n][2] > width_screen:
        Ball_Parameters[n][4] = - Ball_Parameters[n][4]
        Ball_Parameters[n][0] += Ball_Parameters[n][4] / FPS
    if Ball_Parameters[n][1] + Ball_Parameters[n][2] > height_screen:
        Ball_Parameters[n][5] = - Ball_Parameters[n][5]
        Ball_Parameters[n][1] += Ball_Parameters[n][5] / FPS


# checking if we hit the ball
def ball_handle_event_hit(event, i):
    global hit
    global Ball_Parameters
    if (event.pos[0] - Ball_Parameters[i][0]) ** 2 + \
            (event.pos[1] - Ball_Parameters[i][1]) ** 2 < Ball_Parameters[i][2] ** 2:
        hit += 1
        create_ball(i)
        return True
    return False


# number of special shapes
shape_q = 8
Shape_Parameters = [0] * shape_q
for i in range(shape_q):
    Shape_Parameters[i] = [0] * 10


# creates shape which is a polygon with random number of angles
def create_shape(n):
    global Shape_Parameters
    Shape_Parameters[n][0] = randint(100, 700)  # x
    Shape_Parameters[n][1] = randint(100, 500)  # y
    Shape_Parameters[n][2] = randint(Rmin, (Rmax + 3 * Rmin) // 4)  # radius
    shape_change_color(n)  # colors
    Shape_Parameters[n][4] = randint(80, 300) * (randint(0, 1) * 2 - 1)  # vx - speed xlabel
    Shape_Parameters[n][5] = randint(80, 300) * (randint(0, 1) * 2 - 1)  # vy - speed ylabel
    Shape_Parameters[n][6] = randint(3, 9)  # quantity of angles
    Shape_Parameters[n][7] = randint(0, round(2 * m.pi))  # rotation angle
    Shape_Parameters[n][8] = randint(2, round(4 * m.pi)) * (
                randint(0, 1) * 2 - 1)  # OMEGA motherfucker do you speak it???
    Shape_Parameters[n][9] = pygame.time.get_ticks()


# draws this shape
def draw_shape(n):
    global Shape_Parameters
    # defines vertices of the polygon
    shape_vertices = [0] * Shape_Parameters[n][6]
    # counting an angle between two vertices
    alpha = 2 * m.pi / Shape_Parameters[n][6]
    # creating a list of vertices
    for i in range(Shape_Parameters[n][6]):
        shape_vertices[i] = (
            round(Shape_Parameters[n][0] + Shape_Parameters[n][2] * m.cos(Shape_Parameters[n][7] + alpha * i)),
            round(Shape_Parameters[n][1] + Shape_Parameters[n][2] * m.sin(Shape_Parameters[n][7] + alpha * i)))
    polygon(screen, Shape_Parameters[n][3], shape_vertices)


# makes the world fly (moving and rotating the shape)
def move_shape(n):
    global Shape_Parameters
    Shape_Parameters[n][0] += Shape_Parameters[n][4] / FPS
    Shape_Parameters[n][1] += Shape_Parameters[n][5] / FPS
    # implementing rotation
    Shape_Parameters[n][7] += Shape_Parameters[n][8] / FPS
    if Shape_Parameters[n][0] - Shape_Parameters[n][2] < 0:
        Shape_Parameters[n][4] = - Shape_Parameters[n][4]
        Shape_Parameters[n][0] += 3 * Shape_Parameters[n][4] / FPS
    if Shape_Parameters[n][1] - Shape_Parameters[n][2] < 0:
        Shape_Parameters[n][5] = - Shape_Parameters[n][5]
        Shape_Parameters[n][1] += 3 * Shape_Parameters[n][5] / FPS
    if Shape_Parameters[n][0] + Shape_Parameters[n][2] > width_screen:
        Shape_Parameters[n][4] = - Shape_Parameters[n][4]
        Shape_Parameters[n][0] += 3 * Shape_Parameters[n][4] / FPS
    if Shape_Parameters[n][1] + Shape_Parameters[n][2] > height_screen:
        Shape_Parameters[n][5] = - Shape_Parameters[n][5]
        Shape_Parameters[n][1] += 3 * Shape_Parameters[n][5] / FPS


# checking if we hit the shape
def shape_handle_event_hit(event, i):
    global hit
    global Shape_Parameters
    # counting an angle between two vertices
    alpha = 2 * m.pi / Shape_Parameters[i][6]
    f = True
    for j in range(Shape_Parameters[i][6]):
        # counting vector between 2 neighbouring vertices
        a_x = Shape_Parameters[i][0] + Shape_Parameters[i][2] * m.cos(Shape_Parameters[i][7] + alpha * j)
        a_y = Shape_Parameters[i][1] + Shape_Parameters[i][2] * m.sin(Shape_Parameters[i][7] + alpha * j)
        b_x = Shape_Parameters[i][0] + Shape_Parameters[i][2] * m.cos(Shape_Parameters[i][7] + alpha * (j + 1))
        b_y = Shape_Parameters[i][1] + Shape_Parameters[i][2] * m.sin(Shape_Parameters[i][7] + alpha * (j + 1))
        # counting vector between the first neighbouring vertex and click position
        ev_point_x = event.pos[0] - a_x
        ev_point_y = event.pos[1] - a_y
        v_x = b_x - a_x
        v_y = b_y - a_y
        # counting the determinant(oriented area)
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


# defining dimensions of the score and its font_size
x_score = 600
y_score = 500
font_size_score = 22

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
    draw_inscription()
    for n in range(balls_q + shape_q):
        n1 = n - balls_q
        if n < balls_q:
            if Ball_Parameters[n][2] > Rmax:
                miss += 1
                create_ball(n)
            elif (pygame.time.get_ticks() - Ball_Parameters[n][6]) > 60:  # Увеличение
                Ball_Parameters[n][2] += 1
                Ball_Parameters[n][6] = pygame.time.get_ticks()
            ball_change_color(n)
            move_ball(n)
            draw_ball(n)
        elif n1 >= 0:
            if Shape_Parameters[n1][2] > Rmax:
                miss += 1
                create_shape(n1)
            elif (pygame.time.get_ticks() - Shape_Parameters[n1][9]) > 60:  # Увеличение
                Shape_Parameters[n1][2] += 1
                Shape_Parameters[n1][9] = pygame.time.get_ticks()
            shape_change_color(n1)
            move_shape(n1)
            draw_shape(n1)
    score(x_score, y_score, font_size_score)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
