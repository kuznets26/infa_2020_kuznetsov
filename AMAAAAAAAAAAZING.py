import pygame
from pygame.draw import *

pygame.init()

# drawing the screen and filling it
FPS = 60
screen = pygame.display.set_mode((800, 600))
rect(screen, (214, 214, 208), (0, 0, 800, 600))

# a boy holding a sign
circle(screen, (191, 45, 0), (400, 650), 240, 0)  # body
circle(screen, (227, 180, 136), (400, 300), 180, 0)  # head
polygon(screen, (227, 180, 136), [(570, 470), (700, 4), (720, 4), (600, 480)])  # right hand
circle(screen, (227, 180, 136), (690, 65), 40)
circle(screen, (255, 229, 204), (690, 65), 40, 1)
polygon(screen, (227, 180, 136), [(230, 470), (100, 4), (80, 4), (200, 480)])  # left hand
circle(screen, (227, 180, 136), (110, 65), 40)
circle(screen, (255, 229, 204), (110, 65), 40, 1)
polygon(screen, (191, 45, 0), [(510, 480), (560, 400),
                               (645, 445), (650, 510), (570, 540)])  # right T-shirt
polygon(screen, (0, 0, 0), [(510, 480), (560, 400),
                            (645, 445), (650, 510), (570, 540)], 1)  # line
polygon(screen, (191, 45, 0), [(290, 480), (240, 400),
                               (155, 445), (150, 510), (230, 540)])  # left T-shirt
polygon(screen, (0, 0, 0), [(290, 480), (240, 400),
                            (155, 445), (150, 510), (230, 540)], 1)  # line
# drawing eyes
ellipse(screen, (143, 161, 255), (420, 220, 90, 80))  # right eye
ellipse(screen, (0, 0, 0), (420, 220, 90, 80), 1)
ellipse(screen, (143, 161, 255), (290, 220, 90, 80))  # left eye
ellipse(screen, (0, 0, 0), (290, 220, 90, 80), 1)
ellipse(screen, (0, 0, 0), (453, 255, 25, 20))  # right small eye
ellipse(screen, (0, 0, 0), (323, 255, 25, 20))
# drawing nose and mouth
polygon(screen, (94, 50, 0), [(400, 342), (417, 310), (383, 310)])
polygon(screen, (64, 34, 1), [(400, 342), (417, 310), (383, 310)], 1)
polygon(screen, (212, 2, 2), [(400, 420), (500, 370), (300, 370)])
polygon(screen, (112, 0, 0), [(400, 420), (500, 370), (300, 370)], 1)
# lots of violet triangles over head - a boy`s really a punk!
polygon(screen, (168, 61, 235), [(250, 204), (245, 150), (295, 165)])
polygon(screen, (0, 0, 0), [(250, 204), (245, 150), (295, 165)], 1)
polygon(screen, (168, 61, 235), [(280, 175), (280, 120), (325, 150)])
polygon(screen, (0, 0, 0), [(280, 175), (280, 120), (325, 150)], 1)
polygon(screen, (168, 61, 235), [(310, 155), (315, 105), (355, 134)])
polygon(screen, (0, 0, 0), [(310, 155), (315, 105), (355, 134)], 1)
polygon(screen, (168, 61, 235), [(340, 138), (350, 90), (382, 125)])
polygon(screen, (0, 0, 0), [(340, 138), (350, 90), (382, 125)], 1)
polygon(screen, (168, 61, 235), [(370, 130), (385, 90), (410, 125)])
polygon(screen, (0, 0, 0), [(370, 130), (385, 90), (410, 125)], 1)
polygon(screen, (168, 61, 235), [(550, 204), (555, 150), (505, 165)])
polygon(screen, (0, 0, 0), [(550, 204), (555, 150), (505, 165)], 1)
polygon(screen, (168, 61, 235), [(520, 175), (520, 120), (475, 150)])
polygon(screen, (0, 0, 0), [(520, 175), (520, 120), (475, 150)], 1)
polygon(screen, (168, 61, 235), [(490, 155), (485, 105), (445, 134)])
polygon(screen, (0, 0, 0), [(490, 155), (485, 105), (445, 134)], 1)
polygon(screen, (168, 61, 235), [(430, 130), (415, 90), (390, 125)])
polygon(screen, (0, 0, 0), [(430, 130), (415, 90), (390, 125)], 1)
polygon(screen, (168, 61, 235), [(460, 138), (450, 90), (418, 125)])
polygon(screen, (0, 0, 0), [(460, 138), (450, 90), (418, 125)], 1)

# a sign "Python`s amazing
polygon(screen, (132, 229, 5), [(0, 0), (800, 0),
                                (800, 70), (0, 70)])  # banner
inscription_font = pygame.font.SysFont('Arial Black', 64)
inscription = inscription_font.render("PYTHON is AMAZING", 5, (0, 0, 0))  # inscription
screen.blit(inscription, (30, -12))  # where to

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
