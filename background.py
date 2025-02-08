import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('sprites/background_1_1.png')
        self.image = pygame.transform.scale(self.image,
                                                 (1200, 800))
        self.image_index = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

    def output(self, mask):
        self.screen.blit(self.image, self.rect)
        if pygame.sprite.collide_mask(self, mask):
            if self.image_index != 4:
                self.image = pygame.image.load(f'sprites/background_1_{self.image_index}.png')
                self.image = pygame.transform.scale(self.image,
                                                    (1200, 800))

                self.image_index += 1
            if self.image_index == 4:
                self.image_index = 3
        else:
            if self.image_index != 0:
                self.image = pygame.image.load(f'sprites/background_1_{self.image_index}.png')
                self.image = pygame.transform.scale(self.image,
                                                    (1200, 800))
                self.image_index -= 1

        if self.image_index == 0:
            self.image_index = 1