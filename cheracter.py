import pygame


class Lamp(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("sprites/beg1.png")
        self.aura = pygame.image.load("sprites/aura.png")
        self.aura = pygame.transform.scale(self.aura,
                                           (2048 * 3, 2048 * 3))
        self.aura_rect = self.aura.get_rect()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 400
        self.aura_rect.centerx = self.screen_rect.centerx - 400
        self.aura_rect.centery = self.screen_rect.bottom - 195
        self.center = float(self.rect.centerx)
        self.rect.centery = self.screen_rect.bottom - 195

        # всякие проверочные переменный
        self.move_right = False
        self.move_left = False
        self.move_jump = False
        self.walk_index = 2
        self.stand_index = 0
        self.stand_check = True
        self.collide = False
        self.hide_index = False
        self.hide_count = 0

    def output(self, back):
        # отрисовка персонажа и аурыoooooo
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.aura, self.aura_rect)

    def update(self, back):
        if self.hide_index == False:
            if self.stand_check == True:
                # анимация бездействия персонажа
                self.image = pygame.image.load(f"sprites/stoyka{self.stand_index // 6 + 1}.png")
                self.image = pygame.transform.scale(self.image,
                                                    (54, 162))
                self.stand_index = (self.stand_index + 1) % 12
            else:
                # анимация ходьбы вправо
                if self.move_right and self.rect.right < self.screen_rect.right:
                    self.center += 9
                    self.image = pygame.image.load(f"sprites/beg{self.walk_index // 2}.png")
                    self.image = pygame.transform.scale(self.image,
                                                        (78, 150))
                    self.walk_index = (self.walk_index + 1) % 8
                    if self.walk_index < 2:
                        self.walk_index = 2
                # анимация ходьбы в лево
                if self.move_left and self.rect.left > self.screen_rect.left:
                    self.center -= 9
                    self.image = pygame.image.load(f"sprites/beg{self.walk_index // 2 + 3}.png")
                    self.image = pygame.transform.scale(self.image,
                                                        (78, 150))
                    self.walk_index = (self.walk_index + 1) % 8
                    if self.walk_index < 2:
                        self.walk_index = 2
                self.rect.centerx = self.center
                self.aura_rect.centerx = self.center

        else:
            # анимация того как персонаж прячется
            if self.hide_count != 18:
                self.image = pygame.image.load(f"sprites/hide/hide{self.hide_count // 2 + 1}.png")
                self.image = pygame.transform.scale(self.image,(126, 180))
                self.hide_count = self.hide_count + 1

        # проверка на касание с дверьми
        if pygame.sprite.collide_mask(self, back):
            # телепортация в зависимости от координат
            if back.image_index == 3:
                if self.rect.centerx < 600 and self.rect.centery > 400:
                    self.rect.centerx = 80
                    self.rect.centery = self.aura_rect.centery = 260
                    self.aura_rect.centerx = 80
                    self.aura_rect.centery = 260
                    self.center = self.rect.centerx
                elif self.rect.centerx > 600 and self.rect.centery > 400:
                    self.rect.centerx = 1120
                    self.rect.centery = self.aura_rect.centery = 260
                    self.aura_rect.centerx = 1120
                    self.aura_rect.centery = 260
                    self.center = self.rect.centerx
                elif self.rect.centerx < 600 and self.rect.centery < 400:
                    self.rect.centerx = 80
                    self.rect.centery = self.aura_rect.centery = self.screen_rect.bottom - 195
                    self.aura_rect.centerx = 80
                    self.center = self.rect.centerx
                elif self.rect.centerx > 600 and self.rect.centery < 400:
                    self.rect.centerx = 1120
                    self.rect.centery = self.aura_rect.centery = self.screen_rect.bottom - 195
                    self.aura_rect.centerx = 1120
                    self.center = self.rect.centerx

        # elif self.collide:
        #     if self.move_right and self.rect.right < self.screen_rect.right:
        #         self.center += 7
        #     elif self.move_left and self.rect.left > self.screen_rect.left:
        #         self.center -= 7
        #     if self.jump_index > 0:
        #         if self.collide_2 == True and self.jump_index != 15:
        #             self.rect.centery += 2
        #             self.jump_index -= 2
        #         else:
        #             print('up')
        #             self.jump_index -= 2
        #             self.rect.centery -= 15
        #     elif self.jump_index == 0:
        #         self.jump_index -= 0.2
        #     elif -1 > self.jump_index > -10:
        #         self.rect.centery += 12
        #         self.jump_index -= 2
        #     else:
        #         self.jump_index = 15
        #         self.move_jump = False
        #     self.rect.centerx = self.center

    def update_aura(self, count):
        if count > 0:
            self.aura = pygame.transform.scale(self.aura,
                                               (2048 * 3 - (2048 * 3 * 0.005 * count),
                                                2048 * 3 - (2048 * 3 * 0.005 * count)))
            self.aura_rect = self.aura.get_rect()
            self.aura_rect.centerx = self.rect.centerx + 35
            self.aura_rect.centery = self.rect.centery + 5
        else:
            self.aura = pygame.transform.scale(pygame.image.load("sprites/aura.png"),
                                               (2048 * 3, 2048 * 3))
            self.aura_rect = self.aura.get_rect()
            self.aura_rect.centerx = self.rect.centerx
            self.aura_rect.centery = self.rect.centery
