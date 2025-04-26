import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.rect = self.surf.get_rect()








