######################################################################
# Author: Jairus Harrison, Aaron Whitaker
# Username: Harrisonj2, whitakera2
#
# Assignment: p01-final-project
#

######################################################################
# Acknowledgements:
#
####################################################################################
import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        """
        Represents the player in the game.

        :param screen_size: Screen size, for keeping character on the screen
        """
        super().__init__()
        self.screen_size = screen_size
        self.surf = pygame.image.load("image/up.png").convert_alpha() #image goes here in quotes
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)
        self.screen_height = 600
        self.screen_width = 600
        self.speed = 5.8


    def movement(self, keys):
        """
        Handles up, down, left, right movement events from the user

        :param keys: key presses from pygame event listener
        :return: None none
        """
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.surf = pygame.image.load("image/left.png").convert_alpha()  # image goes here in quotes
            self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.surf = pygame.image.load("image/right.png").convert_alpha()  # image goes here in quotes
            self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.surf = pygame.image.load("image/up.png").convert_alpha()  # image goes here in quotes
            self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.surf = pygame.image.load("image/downward.png").convert_alpha()  # image goes here in quotes
            self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)

            # Border collision
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(self.screen_width, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(self.screen_height, self.rect.bottom)