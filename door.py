import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        # Create a transparent surface for collision logic only (optional)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Fully transparent
        self.rect = self.image.get_rect(topleft=position)










