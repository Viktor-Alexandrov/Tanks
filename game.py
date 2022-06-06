import sys

import pygame
import config

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Танчики')
screen = pygame.display.set_mode(config.WINDOW_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    pygame.display.update()

    clock.tick(config.FPS)

