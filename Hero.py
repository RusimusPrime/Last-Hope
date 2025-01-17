import pygame

class MainCharacter:
    def __init__(self, attack, defence, speed, hp, path, x, y):
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.hp = hp
        self.pos = (x, y)
        image = pygame.transform.scale(pygame.image.load(path), (50, 100))

    def attack(self):
        pass

    def change_attack(self):
        pass

    def take_damage(self, attack):
        self.hp -= attack * self.defence / 100

    def check_health(self):
        return self.hp > 0

    def check_pos(self):
        return self.pos

    def update_pos(self, x, y):
        self.pos = (x, y)
