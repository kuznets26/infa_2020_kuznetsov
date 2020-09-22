import pygame
from pygame.draw import *

pygame.init()

FPS = 60
screen = pygame.display.set_mode((800,600))
rect(screen, (214, 214, 208), (0,0,800,600))

polygon(screen, (132, 229, 5), [(0, 0), (800, 0), (800, 70), (0, 70)] )

circle(screen, (191, 45, 0), (400, 650), 240, 0)
circle(screen, (227, 180, 136), (400, 300), 180, 0)






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

