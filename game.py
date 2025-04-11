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
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill( )
        self.clock = pygame.time.Clock()

def main():

    game = Game()

if __name__ == "__main__":
    main()
