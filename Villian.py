import pygame


class MinorVillain :
    def __init__(self, attack, defence, speed, hp, path, width, height, x, y, on_the_screen=True):
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.hp = hp
        self.image = pygame.transform.scale(pygame.image.load(path), (width, height))
        self.on_the_screen = on_the_screen
        self.pos = (x, y)

    def attack(self):
        pass

    def visible(self):
        if self.on_the_screen:
            pass  # Если переменная ровна True то отрисовывать спрйт

    def take_damage(self, attack):
        self.hp -= attack * self.defence / 100

    def check_health(self):
        return self.hp > 0

    def check_screen(self):
        return self.on_the_screen

    def get_pos(self):
        return self.pos


