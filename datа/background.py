import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, screen, n):
        super().__init__()
        self.screen = screen
        self.n = n
        self.image = pygame.image.load(f"datа/images/background_{n % 2 + 1}_1.png")
        self.image = pygame.transform.scale(self.image,
                                            (1200, 800))
        self.back = pygame.image.load("datа/images/back.png") if n % 2 == 0 else pygame.image.load(
            "datа/images/back_2.jpg")
        self.back = pygame.transform.scale(self.back,
                                           (1200, 800))
        self.image_index = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.off = False
        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

    def output(self, mask):
        # отрисовка фонов
        self.screen.blit(self.back, self.rect)
        self.screen.blit(self.image, self.rect)
        # анимация открытия дверей
        if pygame.sprite.collide_mask(self, mask):
            if self.image_index != 4:
                self.image = pygame.image.load(f"datа/background_{self.n % 2 + 1}_{self.image_index}.png")
                self.image = pygame.transform.scale(self.image,
                                                    (1200, 800))

                self.image_index += 1
            if self.image_index == 4:
                self.image_index = 3
        else:
            if self.image_index != 0:
                self.image = pygame.image.load(f"datа/images/background_{self.n % 2 + 1}_{self.image_index}.png")
                self.image = pygame.transform.scale(self.image,
                                                    (1200, 800))
                self.image_index -= 1
        if self.image_index == 0:
            self.image_index = 1
