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

import pygame,random,math

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
        self.surf = pygame.image.load('image/lamb.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0] // 4, self.screen_size[1] // 4)
        self.path = random.choice(self.directions)
        self.position = [0, 0]

    def get_direction(self):
        """
        Keeps the NPC on the screen.

        :return: None
        """
        if self.rect.bottom >= self.screen_size[1]:
            # Bottom
            self.path = "north"
        if self.rect.top <= 0:
            # Top
            self.path = "south"
        if self.rect.left <= 0:
            # Left
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            # Right
            self.path = "west"
        elif random.random() > .95:
            # Randomly change direction 5% of the time
            self.path = random.choice(self.directions)

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

        self.get_direction()

class Good_NPC(NPC):
    def __init__(self, screen_size):
        super().__init__(screen_size)


class Bad_NPC(NPC):
    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.surf = pygame.image.load('image/Monster.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def movement(self, player_position):
        """
        Moves the NPC toward the player.

        :param player_position: Tuple (x, y) of the player's current position
        :return: None
        """
        dx = player_position[0] - self.rect.centerx
        dy = player_position[1] - self.rect.centery
        distance = math.hypot(dx, dy)

        chase_radius = 200

        if distance < chase_radius and distance != 0:
            dx /= distance
            dy /= distance
            self.rect.move_ip(dx * self.move_distance, dy * self.move_distance)