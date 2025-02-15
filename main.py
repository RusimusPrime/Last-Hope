from game_test import *
import sqlite3
import sys

class Menu(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        pygame.draw.rect(screen, 'white', (406, 640, 388, 28))
        pygame.draw.rect(screen, 'white', (406, 675, 388, 28))
        pygame.draw.rect(screen, 'white', (406, 710, 388, 28))
        screen.blit(pygame.font.SysFont('Arial', 25).render('Начать игру', True, (255, 0, 0)), (540, 640))
        screen.blit(pygame.font.SysFont('Arial', 25).render('Другой уровень', True, (255, 0, 0)), (515, 675))
        screen.blit(pygame.font.SysFont('Arial', 25).render('Лучший результат', True, (255, 0, 0)), (500, 710))
        self.rect1 = pygame.Rect(406, 640, 388, 28)
        self.rect2 = pygame.Rect(406, 675, 388, 28)
        self.rect3 = pygame.Rect(406, 710, 388, 28)
        print(pygame.mouse.get_pos())

    def update(self, mouse):
        if self.rect1.collidepoint(mouse):
            start = 1
            while True:
                if start == 1:
                    work()
                    start = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            start = 1
        elif self.rect2.collidepoint(mouse):
            print('YES')
        elif self.rect3.collidepoint(mouse):
            con = sqlite3.connect("time.sqlite")
            cur = con.cursor()
            result = cur.execute("""SELECT * FROM best_time""").fetchall()
            result = max(result) if result else ''
            if result != '':
                engine = pyttsx3.init()
                text = f"Лучший результат {result} секунд"
                engine.say(text)
                engine.runAndWait()
            else:
                engine = pyttsx3.init()
                text = f"Извините, но пока нет результатов"
                engine.say(text)
                engine.runAndWait()


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Last Hope")
screen.fill('black')
menu = Menu(screen)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            menu.update(mouse)
    pygame.display.update()
    clock.tick(60)
