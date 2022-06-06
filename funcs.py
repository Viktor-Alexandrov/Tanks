import pygame.image


def load_image(title, bg):
    """Загрузка изображения"""
    if bg:
        image = pygame.image.load(
            'assets/sprites/' + title + '.png').convert_alpha()
    else:
        image = pygame.image.load(
            'assets/sprites/' + title + '.png').convert()

    rect = image.get_rect()

    return image, rect
