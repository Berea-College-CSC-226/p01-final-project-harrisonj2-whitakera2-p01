######################################################################
# Author: Jairus Harrison
# Username: harrisonj2
#
# Assignment: p01-final-project
#
######################################################################
# Acknowledgements:
#
# Dr.Scott Heggen
####################################################################################

import pygame
from Npc import NPC
from character import Character
from GUI import MyTkinterApp

class Game:
    def __init__(self):
        self.size = 272, 276
        self.running = True
        pygame.init()
        game_display = pygame.display.set_mode(self.size)
        bg_image = pygame.image.load('image/Starter.jpg')
        self.clock = pygame.time.Clock()
        game_display.blit(bg_image, (0, 0))
        pygame.display.update()
        self.pLayer = Character(self.size)
        self.npc = NPC(self.size)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


def main():

    game = Game()
    game.run()

if __name__ == "__main__":
    main()
