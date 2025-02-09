import pygame



class MinorVillain(pygame.sprite.Sprite):
    def __init__(self, x, y, on_the_screen=True, *group):
        super().__init__(*group)
        self.on_the_screen = on_the_screen
        self.rect = pygame.transform.scale(pygame.image.load('images/enemy2.png'), (128, 128)).get_rect()
        self.direction = 'right'
        self.count = 0
        self.move_count = 0
        self.rect.x, self.rect.y = x, y
        self.size = (114, 200)
        self.current_image = pygame.transform.scale(pygame.image.load('images/enemy1.png'), self.size)
        self.sprites_right = [pygame.transform.scale(pygame.image.load('images/enemy1.png'), self.size),
                              pygame.transform.scale(pygame.image.load('images/enemy2.png'), self.size),
                              pygame.transform.scale(pygame.image.load('images/enemy3.png'), self.size),
                              pygame.transform.scale(pygame.image.load('images/enemy4.png'), self.size)]
        self.sprites_left = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/enemy1.png'), self.size), True, False),
                             pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/enemy2.png'), self.size), True, False),
                             pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/enemy3.png'), self.size), True, False),
                             pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/enemy4.png'), self.size), True, False)]
# 300 - 900
    def update(self, hero):
        if (not hero.hide_index) and -200 < hero.rect.x - self.rect.x < 0 and self.direction == 'left':
            self.rect.x += - 7
            self.count = (self.count + 1) % 12
            self.current_image = self.sprites_left[self.count // 3]

        elif (not hero.hide_index) and 0 < hero.rect.x - self.rect.x < 200 and self.direction == 'right':
            self.rect.x += 7
            self.count = (self.count + 1) % 12
            self.current_image = self.sprites_right[self.count // 3]

        else:
            if self.direction == 'right':
                self.rect.x += 3
                self.move_count = (self.move_count + 1) % 12
                self.current_image = self.sprites_right[self.move_count // 3]

            elif self.direction == 'left':
                self.rect.x += -3
                self.move_count = (self.move_count + 1) % 12
                print(self.move_count)
                self.current_image = self.sprites_left[self.move_count // 3]

            if self.rect.x < 300 or self.rect.x > 700:
                self.direction = 'right' if self.direction == 'left' else 'left'

    def are_sprites_touching(self, sprite2):
        return self.rect.colliderect(sprite2.rect)


