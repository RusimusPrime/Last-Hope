import pygame
from Hero import MainCharacter
from Villian import MinorVillain
import sys, gif_pygame

class Map:
    def __init__(self, background, level):
        screen = pygame.display.set_mode((330, 330))
        gif = gif_pygame.load(background)
        self.level = pygame.transform.scale(pygame.image.load(level), (330, 330))
        while True:
            screen.fill((0, 0, 0))
            gif.render(screen, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(self.level, self.level.get_rect())
            pygame.display.update()
a = Map("background.gif", 'level.png')