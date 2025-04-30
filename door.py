import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, position, size, destination_room):
        super().__init__()
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Transparent
        self.rect = self.image.get_rect(topleft=position)
        self.destination_room = destination_room







