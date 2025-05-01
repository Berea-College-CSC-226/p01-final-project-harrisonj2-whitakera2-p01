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

import pygame
from Npc import Good_NPC, Bad_NPC
from character import Character
import random
from door import Door

class Game:
    def __init__(self):
        self.size = 600,600
        self.running = True
        self.screen_height = 600
        self.screen_width = 600
        pygame.init()
        self.game_display = pygame.display.set_mode(self.size)
        self.bg_image = pygame.image.load('image/Level_1.png')
        self.clock = pygame.time.Clock()
        self.game_display.blit(self.bg_image, (0, 0))
        pygame.display.update()
        self.player = Character(self.size)
        self.rooms_with_spawned_sheep = set()
        self.good_npc = pygame.sprite.Group()  # Create the group first
        self.bad_npc = Bad_NPC(self.size)
        self.text_shown_time = None  # To track when the text was shown
        self.text_displayed = False
        self.doors = pygame.sprite.Group()
        self.current_room = 1
        self.load_room_background()
        self.passed_game = False
        self.spawn_locations = {
            1: (254, 294),
            2: (246, 510),
            3: (386, 508),
            4: (258, 438),
            5: (258, 426),
            6: (228, 402),
            7: (246, 510),
        }


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

            #self.game_display.blit(self.bad_npc.surf, self.bad_npc.rect)

            # Check for collisions
            if pygame.sprite.spritecollide(self.player, self.good_npc, True) and not self.text_displayed:
                # Start showing the text
                self.text_shown_time = pygame.time.get_ticks()  # Capture the time when collision happens
                self.text_displayed = True  # Set the flag that text is displayed

            # Show the text for 3 seconds
            if self.text_displayed:
                font = pygame.font.SysFont("ComicSans", 36)
                txt = font.render("You have caught a lamb", True, "white")
                text_rect = txt.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
                self.game_display.blit(txt, text_rect)

                if pygame.time.get_ticks() - self.text_shown_time > 3000:
                    self.text_displayed = False

            # Show "You passed the game" at the top if in room 7
            if self.passed_game:
                font = pygame.font.SysFont("ComicSans", 40)
                passed_text = font.render("YOU PASSED THE GAME", True, "white")
                self.game_display.blit(passed_text, (self.size[0] // 2 - passed_text.get_width() // 2, 20))




                # Check if 3 seconds have passed
                if pygame.time.get_ticks() - self.text_shown_time > 3000:  # 3000 milliseconds = 3 seconds
                    self.text_displayed = False

            for door in self.doors:
                pygame.draw.rect(self.game_display, (255, 0, 0), door.rect, 2)

            # Check for collisions with any door
            for door in self.doors:
                if self.player.rect.colliderect(door.rect):
                    self.current_room = door.destination_room
                    self.load_room_background()

                    self.player.rect.topleft = self.spawn_locations.get(self.current_room, (0, 0))

                    break

            pygame.display.update()
            self.clock.tick(24)

    def spawn_npc(self, count):
        for i in range(count):
            npc = Good_NPC(self.size)
            npc.rect.topleft = (
                random.randint(0, self.size[0] - npc.rect.width),
                random.randint(0, self.size[1] - npc.rect.height))
            self.good_npc.add(npc)

    def load_room_background(self):

        self.doors.empty()
        self.good_npc.empty()

        # Load room background and NPCs
        if self.current_room == 1:
            self.bg_image = pygame.image.load('image/Level_1.png')
            self.doors.add(Door((290, 90), (20, 20), 2))
            if 1 not in self.rooms_with_spawned_sheep:
                self.spawn_npc(1)
                self.rooms_with_spawned_sheep.add(1)

        elif self.current_room == 2:
            self.bg_image = pygame.image.load('image/Level_2.png')
            self.doors.add(Door((288, 358), (20, 20), 1))
            self.doors.add(Door((476, 100), (20, 20), 3))
            self.doors.add(Door((100, 94), (20, 20), 4))

        elif self.current_room == 3:
            self.bg_image = pygame.image.load('image/Level_3.png')
            self.doors.add(Door((406, 402), (20, 20), 2))
            self.doors.add(Door((182, 64), (20, 20), 5))
            self.doors.add(Door((550, 90), (20, 20), 6))

        elif self.current_room == 4:
            self.bg_image = pygame.image.load('image/Scary_Zone.png')
            self.doors.add(Door((290, 540), (20, 20), 2))


        elif self.current_room == 5:
            self.bg_image = pygame.image.load('image/Lamb_level.png')
            self.doors.add(Door((290, 570), (20, 20), 3))
            if 5 not in self.rooms_with_spawned_sheep:
                self.spawn_npc(8)
                self.rooms_with_spawned_sheep.add(5)

        elif self.current_room == 6:
            self.bg_image = pygame.image.load('image/Level_4.png')
            self.doors.add(Door((252, 572), (20, 20), 3))
            self.doors.add(Door((414, 60), (20, 20), 7))
            if 6 not in self.rooms_with_spawned_sheep:
                self.spawn_npc(3)
                self.rooms_with_spawned_sheep.add(6)


        elif self.current_room == 7:
            self.bg_image = pygame.image.load('image/Exit_1.png')
            self.spawn_npc(30)
            self.passed_game = True



def main():

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
