import pygame
import sqlite3
import datа.control
from datа.cheracter import Lamp
from datа.background import Background
from datа.Villian import MinorVillain
from datа.Springbonie import Bonnie
import cv2
import time
import threading, pyttsx3
import random


def screamer(window):
    video = cv2.VideoCapture("datа/images/screem.mp4")
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


def loading(screen):
    video = cv2.VideoCapture("datа/images/fast_final.gif.mp4")
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
        screen.fill('black')
        screen.blit(video_surf, (475, 300))
        pygame.display.flip()


def work(n):
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Last Hope")
    bg_color = (255, 255, 255)
    clock = pygame.time.Clock()
    fps = 30
    lamp = Lamp(screen)
    back = Background(screen, n)
    koef = random.randint(1, 5)
    enemy = Bonnie(300, 510) if koef == 5 else MinorVillain(300, 510)
    koef = random.randint(1, 5)
    enemy2 = MinorVillain(300, 160) if koef == 5 else MinorVillain(300, 160)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(back)
    all_sprites.add(lamp)
    e_count = 0
    start_time = time.time()
    current_y = 555
    time_y = time.time()
    while True:
        if (not lamp.hide_index) and (enemy.are_sprites_touching(lamp) or enemy2.are_sprites_touching(lamp)):
            screamer(screen)
            loading(screen)
            screen.fill('black')
            best_time = str(abs(start_time - time.time()))[:str(start_time - time.time()).find('.') - 1]
            text = f"Вы прожили {best_time} секунд"

            screen.blit(pygame.font.SysFont("Arial", 50).render("Вы проиграли. " + text,
                                                                True, "white"), (250, 375))
            screen.blit(pygame.font.SysFont("Arial", 30).render("Нажмите пробел для перезапуска",
                                                                True, "white"), (400, 430))
            pygame.display.update()
            engine = pyttsx3.init()
            engine.say(text)
            threading.Thread(target=engine.runAndWait).start()
            con = sqlite3.connect("datа/time.sqlite")
            con.execute("""INSERT INTO best_time (time) VALUES(?)""", (best_time,))
            con.commit()
            return True
        if lamp.hide_index:
            e_count += 1
            lamp.update_aura(e_count)
            if e_count > 100:
                screamer(screen)
                loading(screen)
                screen.fill('black')
                best_time = str(abs(start_time - time.time()))[:str(start_time - time.time()).find('.') - 1]
                text = f"Вы прожили {best_time} секунд"
                screen.blit(pygame.font.SysFont("Arial", 50).render("Вы проиграли. " + text,
                                                                    True, "white"), (250, 375))
                screen.blit(pygame.font.SysFont("Arial", 30).render("Нажмите пробел для перезапуска",
                                                                    True, "white"), (400, 430))
                pygame.display.update()
                engine = pyttsx3.init()
                engine.say(text)
                threading.Thread(target=engine.runAndWait).start()
                con = sqlite3.connect("datа/time.sqlite")
                con.execute("""INSERT INTO best_time (time) VALUES(?)""", (best_time,))
                con.commit()
                return True
        elif e_count != 0:
            e_count = 0
            lamp.update_aura(e_count)
        if lamp.rect.y != current_y and not lamp.hide_index:
            current_y = lamp.rect.y
            time_y = time.time()
        if time.time() - time_y >= 20:
            screamer(screen)
            loading(screen)
            screen.fill('black')
            best_time = str(abs(start_time - time.time()))[:str(start_time - time.time()).find('.') - 1]
            text = f"Вы прожили {best_time} секунд"
            screen.blit(pygame.font.SysFont("Arial", 50).render("Вы проиграли. " + text,
                                                                True, "white"), (250, 375))
            screen.blit(pygame.font.SysFont("Arial", 30).render("Нажмите пробел для перезапуска",
                                                                True, "white"), (400, 430))
            pygame.display.update()
            engine = pyttsx3.init()
            engine.say(text)
            threading.Thread(target=engine.runAndWait).start()
            con = sqlite3.connect("datа/time.sqlite")
            con.execute("""INSERT INTO best_time (time) VALUES(?)""", (best_time,))
            con.commit()
            return True
        datа.control.events(lamp, back)
        enemy.update(lamp)
        enemy2.update(lamp)
        lamp.update(back)
        screen.fill(bg_color)
        all_sprites.draw(screen)
        screen.fill(bg_color)
        back.output(lamp)
        screen.blit(enemy.current_image, enemy.rect)
        screen.blit(enemy2.current_image, enemy2.rect)
        lamp.output()
        pygame.display.flip()
        clock.tick(fps)
