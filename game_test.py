import pygame
import sys

import Controls
from cheracter import Lamp
from background import Background
from Villian import MinorVillain
import cv2
import time
import pyttsx3


def screamer(window):
    video = cv2.VideoCapture("images/screem.mp4")
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    clock = pygame.time.Clock()

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(),
                video_image.shape[1::-1],
                "BGR"
            )
        else:
            run = False
        window.blit(video_surf, (0, 0))
        pygame.display.flip()


def work():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Last Hope")
    bg_color = (255, 255, 255)
    clock = pygame.time.Clock()
    fps = 60
    lamp = Lamp(screen)
    back = Background(screen)
    enemy = MinorVillain(300, 510)
    enemy2 = MinorVillain(300, 160)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(back)
    all_sprites.add(lamp)
    e_count = 0
    start_time = time.time()
    while True:
        if (not lamp.hide_index) and (enemy.are_sprites_touching(lamp) or enemy2.are_sprites_touching(lamp)):
            screamer(screen)
            engine = pyttsx3.init()
            text = f"Вы прожили {str(abs(start_time - time.time()))[:str(start_time - time.time()).find('.')]} секунд"
            engine.say(text)
            engine.runAndWait()
            return True
        if lamp.hide_index:
            e_count += 1
            lamp.update_aura(e_count)
            if e_count > 100:
                screamer(screen)
                engine = pyttsx3.init()
                text = f"Вы прожили {str(abs(start_time - time.time()))[:str(start_time - time.time()).find('.')]} секунд"
                engine.say(text)
                engine.runAndWait()
                return True
        elif e_count != 0:
            e_count = 0
            lamp.update_aura(e_count)
        Controls.events(lamp, back)
        enemy.update(lamp)
        enemy2.update(lamp)
        lamp.update(back)
        screen.fill(bg_color)
        all_sprites.draw(screen)
        Controls.update(screen, bg_color, lamp, back, enemy, enemy2)
        clock.tick(fps)


start = 1
while True:
    if start == 1:
        work()
        start = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = 1
