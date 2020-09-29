import pygame
from pygame.draw import *

pygame.init()

# drawing the screen and filling it
FPS = 60
screen1 = pygame.display.set_mode((1600, 900))
rect(screen1, (214, 214, 208), (0, 0, 1600, 900))


# basic position of a boy is x = 40, y = 30. Remember it when transferring it anywhere.
def transfer(screen, t_shirt_color: tuple, body_color: tuple,
             eye_color: tuple, triangle_color: tuple,
             x: int, y: int, d_c: float):
    # a boy holding a sign
    circle(screen, t_shirt_color, (int(x + 400 * d_c), int(y + 650 * d_c)), int(240 * d_c))  # body
    circle(screen, body_color, (int(x + 400 * d_c), int(y + 300 * d_c)), int(180 * d_c))  # head
    # right hand
    polygon(screen, body_color, [(int(x + 570 * d_c), int(y + 470 * d_c)), (int(x + 700 * d_c), int(y + 40 * d_c)),
                                 (int(x + 720 * d_c), int(y + 40 * d_c)), (int(x + 600 * d_c), int(y + 480 * d_c))])
    circle(screen, body_color, (int(x + 690 * d_c), int(y + 65 * d_c)), int(40 * d_c))
    circle(screen, (255, 229, 204), (int(x + 690 * d_c), int(y + 65 * d_c)), int(40 * d_c), 1)
    # left hand
    polygon(screen, body_color, [(int(x + 230 * d_c), int(y + 470 * d_c)), (int(x + 100 * d_c), int(y + 40 * d_c)),
                                 (int(x + 80 * d_c), int(y + 40 * d_c)), (int(x + 200 * d_c), int(y + 480 * d_c))])
    circle(screen, body_color, (int(x + 110 * d_c), int(y + 65 * d_c)), int(40 * d_c))
    circle(screen, body_color, (int(x + 110 * d_c), int(y + 65 * d_c)), int(40 * d_c), 1)
    polygon(screen, t_shirt_color, [(int(x + 510 * d_c), int(y + 480 * d_c)),
                                    (int(x + 560 * d_c), int(y + 400 * d_c)),
                                    (int(x + 640 * d_c), int(y + 450 * d_c)),
                                    (int(x + 650 * d_c), int(y + 510 * d_c)),
                                    (int(x + 570 * d_c), int(y + 540 * d_c))])  # right T-shirt
    polygon(screen, (0, 0, 0), [(int(x + 510 * d_c), int(y + 480 * d_c)),
                                (int(x + 560 * d_c), int(y + 400 * d_c)),
                                (int(x + 640 * d_c), int(y + 450 * d_c)),
                                (int(x + 650 * d_c), int(y + 510 * d_c)),
                                (int(x + 570 * d_c), int(y + 540 * d_c))], 1)  # line
    polygon(screen, t_shirt_color, [(int(x + 290 * d_c), int(y + 480 * d_c)),
                                    (int(x + 240 * d_c), int(y + 400 * d_c)),
                                    (int(x + 160 * d_c), int(y + 450 * d_c)),
                                    (int(x + 150 * d_c), int(y + 510 * d_c)),
                                    (int(x + 230 * d_c), int(y + 540 * d_c))])  # left T-shirt
    polygon(screen, (0, 0, 0), [(int(x + 290 * d_c), int(y + 480 * d_c)),
                                (int(x + 240 * d_c), int(y + 400 * d_c)),
                                (int(x + 160 * d_c), int(y + 450 * d_c)),
                                (int(x + 150 * d_c), int(y + 510 * d_c)),
                                (int(x + 230 * d_c), int(y + 540 * d_c))], 1)  # line
    # drawing eyes
    ellipse(screen, eye_color, (int(x + 420 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)))  # right eye
    ellipse(screen, (0, 0, 0), (int(x + 420 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)), 1)
    ellipse(screen, eye_color, (int(x + 290 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)))  # left eye
    ellipse(screen, (0, 0, 0), (int(x + 290 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)), 1)
    ellipse(screen, (0, 0, 0),
            (int(x + 453 * d_c), int(y + 255 * d_c), int(25 * d_c), int(20 * d_c)))  # right small eye
    ellipse(screen, (0, 0, 0), (int(x + 323 * d_c), int(y + 255 * d_c), int(25 * d_c), int(20 * d_c)))  # left small eye
    # drawing nose and mouth
    polygon(screen, (94, 50, 0), [(int(x + 400 * d_c), int(y + 342 * d_c)),
                                  (int(x + 417 * d_c), int(y + 310 * d_c)),
                                  (int(x + 383 * d_c), int(y + 310 * d_c))])
    polygon(screen, (64, 34, 1), [(int(x + 400 * d_c), int(y + 342 * d_c)),
                                  (int(x + 417 * d_c), int(y + 310 * d_c)),
                                  (int(x + 383 * d_c), int(y + 310 * d_c))], 1)
    polygon(screen, (212, 2, 2), [(int(x + 400 * d_c), int(y + 420 * d_c)),
                                  (int(x + 500 * d_c), int(y + 370 * d_c)),
                                  (int(x + 300 * d_c), int(y + 370 * d_c))])
    polygon(screen, (112, 0, 0), [(int(x + 400 * d_c), int(y + 420 * d_c)),
                                  (int(x + 500 * d_c), int(y + 370 * d_c)),
                                  (int(x + 300 * d_c), int(y + 370 * d_c))], 1)
    # lots of violet triangles over head - a boy`s really a punk!
    polygon(screen, triangle_color, [(int(x + 250 * d_c), int(y + 204 * d_c)),
                                     (int(x + 245 * d_c), int(y + 150 * d_c)),
                                     (int(x + 295 * d_c), int(y + 165 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 250 * d_c), int(y + 204 * d_c)),
                                (int(x + 245 * d_c), int(y + 150 * d_c)),
                                (int(x + 295 * d_c), int(y + 165 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 280 * d_c), int(y + 175 * d_c)),
                                     (int(x + 280 * d_c), int(y + 120 * d_c)),
                                     (int(x + 325 * d_c), int(y + 150 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 280 * d_c), int(y + 175 * d_c)),
                                (int(x + 280 * d_c), int(y + 120 * d_c)),
                                (int(x + 325 * d_c), int(y + 150 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 310 * d_c), int(y + 155 * d_c)),
                                     (int(x + 315 * d_c), int(y + 105 * d_c)),
                                     (int(x + 355 * d_c), int(y + 134 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 310 * d_c), int(y + 155 * d_c)),
                                (int(x + 315 * d_c), int(y + 105 * d_c)),
                                (int(x + 355 * d_c), int(y + 134 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 340 * d_c), int(y + 138 * d_c)),
                                     (int(x + 350 * d_c), int(y + 90 * d_c)),
                                     (int(x + 382 * d_c), int(y + 125 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 340 * d_c), int(y + 138 * d_c)),
                                (int(x + 350 * d_c), int(y + 90 * d_c)),
                                (int(x + 382 * d_c), int(y + 125 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 370 * d_c), int(y + 130 * d_c)),
                                     (int(x + 385 * d_c), int(y + 90 * d_c)),
                                     (int(x + 410 * d_c), int(y + 125 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 370 * d_c), int(y + 130 * d_c)),
                                (int(x + 385 * d_c), int(y + 90 * d_c)),
                                (int(x + 410 * d_c), int(y + 125 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 550 * d_c), int(y + 204 * d_c)),
                                     (int(x + 555 * d_c), int(y + 150 * d_c)),
                                     (int(x + 505 * d_c), int(y + 165 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 550 * d_c), int(y + 204 * d_c)),
                                (int(x + 555 * d_c), int(y + 150 * d_c)),
                                (int(x + 505 * d_c), int(y + 165 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 520 * d_c), int(y + 175 * d_c)),
                                     (int(x + 520 * d_c), int(y + 120 * d_c)),
                                     (int(x + 475 * d_c), int(y + 150 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 520 * d_c), int(y + 175 * d_c)),
                                (int(x + 520 * d_c), int(y + 120 * d_c)),
                                (int(x + 475 * d_c), int(y + 150 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 490 * d_c), int(y + 155 * d_c)),
                                     (int(x + 485 * d_c), int(y + 105 * d_c)),
                                     (int(x + 445 * d_c), int(y + 134 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 490 * d_c), int(y + 155 * d_c)),
                                (int(x + 485 * d_c), int(y + 105 * d_c)),
                                (int(x + 445 * d_c), int(y + 134 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 430 * d_c), int(y + 130 * d_c)),
                                     (int(x + 415 * d_c), int(y + 90 * d_c)),
                                     (int(x + 390 * d_c), int(y + 125 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 430 * d_c), int(y + 130 * d_c)),
                                (int(x + 415 * d_c), int(y + 90 * d_c)),
                                (int(x + 390 * d_c), int(y + 125 * d_c))], 1)
    polygon(screen, triangle_color, [(int(x + 460 * d_c), int(y + 138 * d_c)),
                                     (int(x + 450 * d_c), int(y + 90 * d_c)),
                                     (int(x + 418 * d_c), int(y + 125 * d_c))])
    polygon(screen, (0, 0, 0), [(int(x + 460 * d_c), int(y + 138 * d_c)),
                                (int(x + 450 * d_c), int(y + 90 * d_c)),
                                (int(x + 418 * d_c), int(y + 125 * d_c))], 1)


def sign(screen, x1: int, y1: int, d_c: float):
    # a sign "Python`s amazing
    polygon(screen, (132, 229, 5), [(x1, int(y1 - 50 * d_c)), (int(x1 + 1400 * d_c), int(y1 - 50 * d_c)),
                                    (int(x1 + 1400 * d_c), int(y1 + 50 * d_c)), (x1, int(y1 + 50 * d_c))])  # banner
    inscription_font = pygame.font.SysFont('Arial Black', int(82 * d_c))
    inscription = inscription_font.render("PYTHON IS REALLY AMAZING", 5, (0, 0, 0))  # inscription
    screen.blit(inscription, (int(x1 + 35 * d_c), int(y1 + (-60) * d_c)))  # where to


transfer(screen1, (177, 221, 252), (252, 252, 202), (67, 195, 250), (87, 24, 4), 100, 200, 1)
transfer(screen1, (223, 227, 5), (247, 235, 121), (67, 240, 220), (7, 140, 36), 700, 200, 1)
sign(screen1, 100, 200, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
