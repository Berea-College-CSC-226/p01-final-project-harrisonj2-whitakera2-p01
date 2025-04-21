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

class Game:
    def __init__(self):
        self.size = 600,600
        self.running = True
        pygame.init()
        self.game_display = pygame.display.set_mode(self.size)
        self.bg_image = pygame.image.load('image/resized_image_600x600.png')
        self.clock = pygame.time.Clock()
        self.game_display.blit(self.bg_image, (0, 0))
        pygame.display.update()
        self.player = Character(self.size)
        self.good_npc = Good_NPC(self.size)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.player.movement(pygame.key.get_pressed())
            self.good_npc.movement()
            self.game_display.blit(self.bg_image, (0, 0))
            self.game_display.blit(self.player.surf, self.player.rect)
            self.game_display.blit(self.good_npc.surf, self.good_npc.rect)
            pygame.display.update()
            self.clock.tick(24)




def main():

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
