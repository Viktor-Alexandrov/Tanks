import sys

import pygame
import config
import funcs

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Танчики')
screen = pygame.display.set_mode(config.WINDOW_SIZE)

bg_image, bg_rect = funcs.load_image('background_image', False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_image, bg_rect)

    pygame.display.update()

    clock.tick(config.FPS)

