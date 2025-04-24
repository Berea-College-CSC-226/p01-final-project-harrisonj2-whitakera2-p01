######################################################################
# Author: Jairus Harrison, Aaron, Whitaker
# Username: harrisonj2, whitakera2
#
# Assignment: p01-final-project
#
######################################################################
# Acknowledgements:
#
# Dr.Scott Heggen
####################################################################################

import pygame
from Npc import Good_NPC
from character import Character
from GUI import MyTkinterApp
import random

class Game:
    def __init__(self):
        self.size = 600,600
        self.running = True
        self.screen_height = 600
        self.screen_width = 600
        pygame.init()
        self.game_display = pygame.display.set_mode(self.size)
        self.bg_image = pygame.image.load('image/resized_image_600x600.png')
        self.clock = pygame.time.Clock()
        self.game_display.blit(self.bg_image, (0, 0))
        pygame.display.update()
        self.player = Character(self.size)
        self.good_npc = self.spawn_npc(5)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.player.movement(pygame.key.get_pressed())
            for npc in self.good_npc:
                npc.movement()
            self.game_display.blit(self.bg_image, (0, 0))
            self.game_display.blit(self.player.surf, self.player.rect)
            for npc in self.good_npc:
                self.game_display.blit(npc.surf, npc.rect)
            pygame.display.update()
            self.clock.tick(24)

    def spawn_npc(self, count):
        names = []
        for i in range(count):
            npc = Good_NPC(self.size)
            npc.rect.topleft = (random.randint(0, self.size[0] - npc.rect.width),
                             random.randint(0, self.size[0] - npc.rect.height))
            names.append(npc)
        return names

def main():

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
