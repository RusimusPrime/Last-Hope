import pygame
import sys
import Controls
from cheracter import Lamp
from background import Background
def work():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Last Hope')
    bg_color = (255, 255, 255)
    clock = pygame.time.Clock()
    fps = 20
    lamp = Lamp(screen)
    back = Background(screen)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(back)
    all_sprites.add(lamp)
    print(all_sprites)

    while True:
        Controls.events(lamp, back)
        lamp.update(back)
        #all_sprites.update()
        screen.fill(bg_color)
        all_sprites.draw(screen)
        Controls.update(screen, bg_color, lamp, back)
        clock.tick(fps)

work()