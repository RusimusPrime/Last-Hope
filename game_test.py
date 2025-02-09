import pygame
import sys
import Controls
from cheracter import Lamp
from background import Background
from Villian import MinorVillain
import Hero
import Map
def work():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Last Hope')
    bg_color = (255, 255, 255)
    clock = pygame.time.Clock()
    fps = 20
    lamp = Lamp(screen)
    back = Background(screen)
    enemy = MinorVillain(300, 500)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(back)
    all_sprites.add(lamp)
    #all_sprites.add(enemy)
    #print(all_sprites)

    while True:
        Controls.events(lamp, back)
        lamp.update(back)
        screen.fill(bg_color)
        all_sprites.draw(screen)
        Controls.update(screen, bg_color, lamp, back, enemy)
        enemy.update(lamp)
        if enemy.are_sprites_touching(lamp):
            print('colide')
        else:
            print('NO')
        clock.tick(fps)

work()