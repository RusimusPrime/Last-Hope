import pygame, sys


def events(cheracter, back):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            cheracter.stand_check = False
            # hide
            if event.key == pygame.K_e:
                cheracter.hide_index = True
                cheracter.rect.centery = cheracter.rect.centery - 9
                cheracter.rect.centerx = cheracter.rect.centerx - 36
            # right
            if event.key == pygame.K_d:
                cheracter.move_right = True
                # cheracter.move_left = False
            # left
            if event.key == pygame.K_a:
                # cheracter.move_right = False
                cheracter.move_left = True
            # jump
            if event.key == pygame.K_SPACE and pygame.sprite.collide_mask(cheracter, back):
                cheracter.move_jump = True

        elif event.type == pygame.KEYUP:
            cheracter.stand_check = True
            # right
            if event.key == pygame.K_d:
                cheracter.move_right = False
            # left
            if event.key == pygame.K_a:
                cheracter.move_left = False
            # hide
            if event.key == pygame.K_e:
                cheracter.hide_index = False
                cheracter.hide_count = 0
                cheracter.rect.centery = cheracter.rect.centery + 9
                cheracter.rect.centerx = cheracter.rect.centerx + 36


def update(screen, bg_color, lamp, back, enemy, enemy2):
    screen.fill(bg_color)
    back.output(lamp)
    screen.blit(enemy.current_image, enemy.rect)
    screen.blit(enemy2.current_image, enemy2.rect)
    lamp.output(back)
    pygame.display.flip()
