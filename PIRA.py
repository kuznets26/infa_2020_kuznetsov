import pygame
from pygame.draw import *

pygame.init()

# drawing the screen and filling it
FPS = 60
screen = pygame.display.set_mode((1400, 700))
rect(screen, (214, 214, 208), (0, 0, 1400, 700))


# basic position of a boy is x = 400, y = 300. Remember it when transferring it anywhere.
def transfer(t_shirt_color: tuple, body_color: tuple,
             eye_color: tuple, triangle_color: tuple,
             x: float, y: float, d_c: float):
    # a boy holding a sign
    circle(screen, t_shirt_color, (x + 400 * d_c, y + 650 * d_c), 240 * d_c, 0)  # body
    circle(screen, body_color, (x + 400 * d_c, y + 300 * d_c), 180 * d_c, 0)  # head
    # right hand
    polygon(screen, body_color, [(x + 570 * d_c, y + 470 * d_c), (x + 700 * d_c, y + 10 * d_c),
                                 (x + 720 * d_c, y + 10 * d_c), (x + 600 * d_c, y + 480 * d_c)])
    circle(screen, body_color, (x + 690 * d_c, y + 65 * d_c), 40 * d_c)
    circle(screen, (255, 229, 204), (x + 690 * d_c, y + 65 * d_c), 40 * d_c, 1)
    # left hand
    polygon(screen, body_color, [(x + 230 * d_c, y + 470 * d_c), (x + 100 * d_c, y + 10 * d_c),
                                 (x + 80 * d_c, y + 10 * d_c), (x + 200 * d_c, y + 480 * d_c)])
    circle(screen, body_color, (x + 110 * d_c, y + 65 * d_c), 40 * d_c)
    circle(screen, body_color, (x + 110 * d_c, y + 65 * d_c), 40 * d_c, 1)
    polygon(screen, t_shirt_color, [(x + 510 * d_c, y + 480 * d_c),
                                    (x + 560 * d_c, y + 400 * d_c),
                                    (x + 645 * d_c, y + 445 * d_c),
                                    (x + 650 * d_c, y + 510 * d_c),
                                    (x + 570 * d_c, y + 540 * d_c)])  # right T-shirt
    polygon(screen, (0, 0, 0), [(x + 510 * d_c, y + 480 * d_c),
                                (x + 560 * d_c, y + 400 * d_c),
                                (x + 645 * d_c, y + 445 * d_c),
                                (x + 650 * d_c, y + 510 * d_c),
                                (x + 570 * d_c, y + 540 * d_c)], 1)  # line
    polygon(screen, t_shirt_color, [(x + 290 * d_c, y + 480 * d_c),
                                    (x + 240 * d_c, y + 400 * d_c),
                                    (x + 155 * d_c, y + 445 * d_c),
                                    (x + 150 * d_c, y + 510 * d_c),
                                    (x + 230 * d_c, y + 540 * d_c)])  # left T-shirt
    polygon(screen, (0, 0, 0), [(x + 290 * d_c, y + 480 * d_c),
                                (x + 240 * d_c, y + 400 * d_c),
                                (x + 155 * d_c, y + 445 * d_c),
                                (x + 150 * d_c, y + 510 * d_c),
                                (x + 230 * d_c, y + 540 * d_c)], 1)  # line
    # drawing eyes
    ellipse(screen, eye_color, (x + 420 * d_c, y + 220 * d_c, 90 * d_c, 80 * d_c))  # right eye
    ellipse(screen, (0, 0, 0), (x + 420 * d_c, y + 220 * d_c, 90 * d_c, 80 * d_c), 1)
    ellipse(screen, eye_color, (x + 290 * d_c, y + 220 * d_c, 90 * d_c, 80 * d_c))  # left eye
    ellipse(screen, (0, 0, 0), (x + 290 * d_c, y + 220 * d_c, 90 * d_c, 80 * d_c), 1)
    ellipse(screen, (0, 0, 0), (x + 453 * d_c, y + 255 * d_c, 25 * d_c, 20 * d_c))  # right small eye
    ellipse(screen, (0, 0, 0), (x + 323 * d_c, y + 255 * d_c, 25 * d_c, 20 * d_c))  # left small eye
    # drawing nose and mouth
    polygon(screen, (94, 50, 0), [(x + 400 * d_c, y + 342 * d_c),
                                  (x + 417 * d_c, y + 310 * d_c), (x + 383 * d_c, y + 310 * d_c)])
    polygon(screen, (64, 34, 1), [(x + 400 * d_c, y + 342 * d_c),
                                  (x + 417 * d_c, y + 310 * d_c), (x + 383 * d_c, y + 310 * d_c)], 1)
    polygon(screen, (212, 2, 2), [(x + 400 * d_c, y + 420 * d_c),
                                  (x + 500 * d_c, y + 370 * d_c), (x + 300 * d_c, y + 370 * d_c)])
    polygon(screen, (112, 0, 0), [(x + 400 * d_c, y + 420 * d_c),
                                  (x + 500 * d_c, y + 370 * d_c), (x + 300 * d_c, y + 370 * d_c)], 1)
    # lots of violet triangles over head - a boy`s really a punk!
    polygon(screen, triangle_color, [(x + 250 * d_c, y + 204 * d_c),
                                     (x + 245 * d_c, y + 150 * d_c), (x + 295 * d_c, y + 165 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 250 * d_c, y + 204 * d_c),
                                (x + 245 * d_c, y + 150 * d_c), (x + 295 * d_c, y + 165 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 280 * d_c, y + 175 * d_c),
                                     (x + 280 * d_c, y + 120 * d_c), (x + 325 * d_c, y + 150 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 280 * d_c, y + 175 * d_c),
                                (x + 280 * d_c, y + 120 * d_c), (x + 325 * d_c, y + 150 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 310 * d_c, y + 155 * d_c),
                                     (x + 315 * d_c, y + 105 * d_c), (x + 355 * d_c, y + 134 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 310 * d_c, y + 155 * d_c),
                                (x + 315 * d_c, y + 105 * d_c), (x + 355 * d_c, y + 134 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 340 * d_c, y + 138 * d_c),
                                     (x + 350 * d_c, y + 90 * d_c), (x + 382 * d_c, y + 125 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 340 * d_c, y + 138 * d_c),
                                (x + 350 * d_c, y + 90 * d_c), (x + 382 * d_c, y + 125 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 370 * d_c, y + 130 * d_c),
                                     (x + 385 * d_c, y + 90 * d_c), (x + 410 * d_c, y + 125 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 370 * d_c, y + 130 * d_c),
                                (x + 385 * d_c, y + 90 * d_c), (x + 410 * d_c, y + 125 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 550 * d_c, y + 204 * d_c),
                                     (x + 555 * d_c, y + 150 * d_c), (x + 505 * d_c, y + 165 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 550 * d_c, y + 204 * d_c),
                                (x + 555 * d_c, y + 150 * d_c), (x + 505 * d_c, y + 165 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 520 * d_c, y + 175 * d_c),
                                     (x + 520 * d_c, y + 120 * d_c), (x + 475 * d_c, y + 150 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 520 * d_c, y + 175 * d_c),
                                (x + 520 * d_c, y + 120 * d_c), (x + 475 * d_c, y + 150 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 490 * d_c, y + 155 * d_c),
                                     (x + 485 * d_c, y + 105 * d_c), (x + 445 * d_c, y + 134 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 490 * d_c, y + 155 * d_c),
                                (x + 485 * d_c, y + 105 * d_c), (x + 445 * d_c, y + 134 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 430 * d_c, y + 130 * d_c),
                                     (x + 415 * d_c, y + 90 * d_c), (x + 390 * d_c, y + 125 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 430 * d_c, y + 130 * d_c),
                                (x + 415 * d_c, y + 90 * d_c), (x + 390 * d_c, y + 125 * d_c)], 1)
    polygon(screen, triangle_color, [(x + 460 * d_c, y + 138 * d_c),
                                     (x + 450 * d_c, y + 90 * d_c), (x + 418 * d_c, y + 125 * d_c)])
    polygon(screen, (0, 0, 0), [(x + 460 * d_c, y + 138 * d_c),
                                (x + 450 * d_c, y + 90 * d_c), (x + 418 * d_c, y + 125 * d_c)], 1)


transfer((177, 221, 252), (252, 252, 202), (67, 195, 250), (87, 24, 4), 0, 40, 1)
transfer((223, 227, 5), (247, 235, 121), (67, 240, 220), (7, 140, 36), 620, 40, 1)

# a sign "Python`s amazing
polygon(screen, (132, 229, 5), [(0, 0), (1400, 0),
                                (1400, 100), (0, 100)])  # banner
inscription_font = pygame.font.SysFont('Arial Black', 82)
inscription = inscription_font.render("PYTHON IS REALLY AMAZING", 5, (0, 0, 0))  # inscription
screen.blit(inscription, (35, -12))  # where to

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
