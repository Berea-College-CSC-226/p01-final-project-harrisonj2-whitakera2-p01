######################################################################
# Author: Jairus Harrison
# Username: Harrisonj2
#
# Assignment: p01-final-project
#

######################################################################
# Acknowledgements:
#
####################################################################################

import pygame,random

class NPC(pygame.sprite.Sprite):
    move_distance = 10
    directions = ["north", "east", "south", "west"]

    def __init__(self, screen_size):
        """
        Represents the Good NPC in the game.

        :param screen_size: size of the window, for ensuring the NPC stays on screen
        """
        print("NPC spawing")
        self.screen_size = screen_size
        super().__init__()
        self.surf = pygame.image.load( ).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0] // 4, self.screen_size[1] // 4)
        self.path = random.choice(self.directions)
        self.position = [0, 0]
