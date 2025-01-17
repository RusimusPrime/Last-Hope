import pygame


class MinorVillain :
    def __init__(self, attack, defence, speed, hp, path, width, height):
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.hp = hp
        image = pygame.transform.scale(pygame.image.load(path), (width, height))

    def attack(self):
        pass

    def take_damage(self, attack):
        self.hp -= attack * self.defence / 100

    def check_health(self):
        return self.hp > 0


