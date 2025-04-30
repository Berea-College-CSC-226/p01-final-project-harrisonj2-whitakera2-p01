######################################################################
# Author: Jairus V. Harrison, Aaron, Whitaker
# Username: harrisonj2, whitakera2
#
# Assignment: p01-final-project
#
######################################################################
# Acknowledgements:
#
# Dr.Scott Heggen
####################################################################################
from enum import nonmember

import pygame
from Npc import Good_NPC, Bad_NPC
from character import Character
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
        self.good_npc = pygame.sprite.Group()  # Create the group first
        self.spawn_npc(5)
        self.bad_npc = Bad_NPC(self.size)
        self.text_shown_time = None  # To track when the text was shown
        self.text_displayed = False





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

            self.game_display.blit(self.bad_npc.surf, self.bad_npc.rect)

            # Check for collision
            if pygame.sprite.spritecollide(self.player, self.good_npc, True) and not self.text_displayed:
                # Start showing the text
                self.text_shown_time = pygame.time.get_ticks()  # Capture the time when collision happens
                self.text_displayed = True  # Set the flag that text is displayed

            # Show the text for 3 seconds
            if self.text_displayed:
                font = pygame.font.SysFont("ComicSans", 36)
                txt = font.render('You have caught a lamb', True, "white")
                text_rect = txt.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
                self.game_display.blit(txt, text_rect)

                # Check if 3 seconds have passed
                if pygame.time.get_ticks() - self.text_shown_time > 3000:  # 3000 milliseconds = 3 seconds
                    self.text_displayed = False

            pygame.display.update()
            self.clock.tick(24)

    def spawn_npc(self, count):
        for i in range(count):
            npc = Good_NPC(self.size)
            npc.rect.topleft = (
                random.randint(0, self.size[0] - npc.rect.width),
                random.randint(0, self.size[1] - npc.rect.height)
            )
            self.good_npc.add(npc)


def main():

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
