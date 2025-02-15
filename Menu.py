import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        pygame.draw.rect(screen, 'white', (406, 640, 388, 28))
        pygame.draw.rect(screen, 'white', (406, 675, 388, 28))
        pygame.draw.rect(screen, 'white', (406, 710, 388, 28))
        screen.blit(pygame.font.SysFont('Arial', 25).render('Начать игру', True, (255, 0, 0)), (540, 640))
        screen.blit(pygame.font.SysFont('Arial', 25).render('Другой уровень', True, (255, 0, 0)), (515, 675))
        screen.blit(pygame.font.SysFont('Arial', 25).render('Лучший результат', True, (255, 0, 0)), (500, 710))
        self.rect = pygame.Rect(406, 640, 388, 28)
        print(pygame.mouse.get_pos())

    def update(self):
        print(pygame.mouse.get_pos())
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print(1234)


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Last Hope")
menu = Menu(screen)
while True:
    menu.update()
    pygame.display.update()