import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

image = pygame.image.load('main.png')
image_rect = image.get_rect()

image_rect.topleft = (50, 50)
x_limit = 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and image_rect.x < x_limit:
        image_rect.x += 5
    if keys[pygame.K_LEFT]:
        image_rect.x -= 5
    if keys[pygame.K_UP]:
        image_rect.y -= 5
    if keys[pygame.K_DOWN]:
        image_rect.y += 5

    screen.fill((255, 255, 255))
    screen.blit(image, image_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
