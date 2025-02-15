import pygame

class MainCharacter:
    def __init__(self, attack=0, defence=0, speed=0, hp=0, path='', x=0, y=0):
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.hp = hp
        self.rect = pygame.transform.scale(pygame.image.load('data/stoyka1.png'), (128, 128)).get_rect()
        #  self.image = pygame.transform.scale(pygame.image.load(path), (50, 100))

    def attack(self):
        for elem in self.cords:
            if abs(elem.get_pos[0] - self.pos[0]) <= 20:
                elem.take_damage(self.attack)

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

    def get_cords_of_villian(self, *args):
        self.cords = args[0]  # формат вида: MinorVillain()
