import pygame,sys 
from pygame.locals import *
from scripts.settings import *

# basic setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("platformer")
fps = 60

player = pygame.Rect(10, 10, 50, 50)
rect = pygame.Rect(300, 10, 100, 50)
color = (0, 255, 0)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.x += 3
    elif keys[pygame.K_LEFT]:
        player.x -= 3

    if player.colliderect(rect):
        color = (0, 0, 255)
    else:
        color = (0, 255, 0)


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player, 3)
    pygame.draw.rect(screen, color, rect, 3)
    pygame.display.update()
    clock.tick(fps)