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

    def movement(self):
        if self.path == "north":
            self.rect.move_ip(0, -self.move_distance)
            self.position[1] -= self.move_distance
        elif self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance
        if self.path == "east":
            self.rect.move_ip(self.move_distance, 0)
            self.position[0] -= self.move_distance
        if self.path == "west":
            self.rect.move_ip(-self.move_distance, 0)
            self.position[0] += self.move_distance

class Good_NPC(NPC):
    def __init__(self, screen_size):
        super().__init__(screen_size)


class Bad_NPC(NPC):
    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.surf = pygame.image.load('images/whiskers.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def movement(self):
        """
                Moves the NPC around.

                :return: None
                """
        if self.path == "north":
            self.rect.move_ip(5, -self.move_distance)
            self.position[1] -= self.move_distance
        elif self.path == "south":
            self.rect.move_ip(5, self.move_distance)
            self.position[1] += self.move_distance
        if self.path == "east":
            self.rect.move_ip(self.move_distance, 5)
            self.position[0] -= self.move_distance
        if self.path == "west":
            self.rect.move_ip(-self.move_distance, 5)
            self.position[0] += self.move_distance

        self.get_direction()