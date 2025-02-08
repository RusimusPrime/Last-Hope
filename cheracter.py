import pygame

class Lamp(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('sprites/beg1.png')
        self.test = pygame.image.load('sprites/тестовый.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.centery = self.screen_rect.bottom - 195
        self.move_right = False
        self.move_left = False
        self.move_jump = False
        self.walk_index = 2
        # self.jump_sprites = 1
        # self.jump_index = 15
        self.stand_index = 0
        self.stand_check = True
        self.collide = False
        # self.collide_2 = False
        self.hide_index = False
        self.hide_count = 0

    def output(self, back):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.test, (100, 100))

    def update(self):
        print(self.hide_index)
        if self.hide_index == False:
            if self.stand_check == True:
                self.image = pygame.image.load(f'sprites/stoyka{self.stand_index // 6 + 1}.png')
                self.image = pygame.transform.scale(self.image,
                                                    (54, 162))
                self.stand_index = (self.stand_index + 1) % 12
            else:
                if self.move_right and self.rect.right < self.screen_rect.right:
                    self.center += 7
                    self.image = pygame.image.load(f'sprites/beg{self.walk_index // 2}.png')
                    self.image = pygame.transform.scale(self.image,
                                                        (78, 150))
                    self.walk_index = (self.walk_index + 1) % 8
                    if self.walk_index < 2:
                        self.walk_index = 2

                if self.move_left and self.rect.left > self.screen_rect.left:
                    self.center -= 7
                    self.image = pygame.image.load(f'sprites/beg{self.walk_index // 2 + 3}.png')
                    self.image = pygame.transform.scale(self.image,
                                                        (78, 150))
                    self.walk_index = (self.walk_index + 1) % 8
                    if self.walk_index < 2:
                        self.walk_index = 2
                self.rect.centerx = self.center

        else:
            if self.hide_count != 27:
                self.image = pygame.image.load(f'sprites/hide/hide{self.hide_count // 3 + 1}.png')
                self.image = pygame.transform.scale(self.image,
                                                    (126, 180))
                self.hide_count = self.hide_count + 1


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
