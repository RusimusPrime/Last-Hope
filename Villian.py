import pygame



class MinorVillain(pygame.sprite.Sprite):
    def __init__(self, x, y, on_the_screen=True, *group):
        super().__init__(*group)
        self.on_the_screen = on_the_screen
        self.rect = pygame.transform.scale(pygame.image.load('images/enemy_2.png'), (128, 128)).get_rect()
        self.direction = 'right'
        self.count = 0
        self.move_count = 0
        self.rect.x, self.rect.y = x, y
        self.current_image = pygame.transform.scale(pygame.image.load('images/enemy_2.png'), (128, 128))
        self.sprites_right = [pygame.transform.scale(pygame.image.load('images/enemy_2.png'), (128, 128)),
                              pygame.transform.scale(pygame.image.load('images/enemy_3.png'), (128, 128)),
                              pygame.transform.scale(pygame.image.load('images/enemy_4.png'), (128, 128))]
        self.sprites_left = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/enemy_2.png'), (128, 128)), True, False),
                             pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/enemy_3.png'), (128, 128)), True, False),
                             pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/enemy_4.png'), (128, 128)), True, False)]

    def update(self, hero):
        if -100 < hero.rect.x - self.rect.x < 0 and self.direction == 'left':
            self.rect.x += - 5
            self.count = (self.count + 1) % 3
            self.current_image = self.sprites_left[self.count]

        elif 0 < hero.rect.x - self.rect.x < 100 and self.direction == 'right':
            self.rect.x += 5
            self.count = (self.count + 1) % 3
            self.current_image = self.sprites_right[self.count]

        else:
            if self.direction == 'right':
                self.rect.x += 2
                self.move_count = (self.move_count + 1) % 50
                self.current_image = self.sprites_right[self.move_count % 3]

            elif self.direction == 'left':
                self.rect.x += -2
                self.move_count = (self.move_count + 1) % 50
                self.current_image = self.sprites_left[self.move_count % 3]

            if self.move_count == 0:
                self.direction = 'right' if self.direction == 'left' else 'left'

    def are_sprites_touching(self, sprite2):
        return self.rect.colliderect(sprite2.rect)


