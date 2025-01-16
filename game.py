import pygame
import sys
import time

pygame.init()

time = pygame.time.Clock()
i = 0
b = 0
jump_r = [
    pygame.image.load('sprites/jump1.png'),
    pygame.image.load('sprites/jump2.png'),
    pygame.image.load('sprites/jump3.png'),
    pygame.image.load('sprites/jump4.png'),
]
jump_l = [

    pygame.image.load('sprites/jump5.png'),
    pygame.image.load('sprites/jump6.png'),
    pygame.image.load('sprites/jump7.png'),
    pygame.image.load('sprites/jump8.png'),
]
beg_r = [
    pygame.image.load('sprites/beg1.png'),
    pygame.image.load('sprites/beg2.png'),
    pygame.image.load('sprites/beg3.png'),
]
beg_l = [
    pygame.image.load('sprites/beg4.png'),
    pygame.image.load('sprites/beg5.png'),
    pygame.image.load('sprites/beg6.png'),
]
stoyka = [
    pygame.image.load('sprites/stoyka1.png'),
    pygame.image.load('sprites/stoyka2.png'),
]
x = 200

player_x = 10
player_y = 450

player_anim_count_beg = 0
player_anim_count_jump = 0
player_anim_count_jump_2 = 0
player_anim_count_stoyka = 0
player_anim_count_stoyka_2 = 0

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption('My game')
isJump = False
jumpcount = 10
player_speed = 10

while True:
    keys = pygame.key.get_pressed()
    screen.fill('white')
    if keys[pygame.K_a] and player_x > 10 and jumpcount == 10:
        screen.blit(beg_l[player_anim_count_beg], (player_x, player_y))
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < 870 and jumpcount == 10:
        screen.blit(beg_r[player_anim_count_beg], (player_x, player_y))
        player_x += player_speed
    elif jumpcount == 10:
        screen.blit(stoyka[player_anim_count_stoyka], (player_x, player_y))

    if player_anim_count_beg == 2:
        player_anim_count_beg = 0
    else:
        player_anim_count_beg += 1

    if isJump == False:
        # if keys[pygame.K_a] and player_x > 10 :
        # screen.blit(beg_l[player_anim_count_beg],(player_x,player_y))
        # player_x -= player_speed
        # elif keys[pygame.K_d] and player_x <870:
        # screen.blit(beg_r[player_anim_count_beg],(player_x,player_y))
        # player_x += player_speed
        if keys[pygame.K_SPACE]:
            isJump = True
        # else :
        # screen.blit(stoyka[player_anim_count_stoyka],(player_x,player_y))

    if jumpcount >= -10 and isJump == True:
        if jumpcount < 0:
            player_y += (jumpcount ** 2) / 6
        else:
            player_y -= (jumpcount ** 2) / 6
        if keys[pygame.K_d] and player_x < 870:
            player_x += player_speed
            screen.blit(jump_r[player_anim_count_jump], (player_x, player_y))
        elif keys[pygame.K_a] and player_x > 10 and keys[pygame.K_SPACE]:
            player_x -= player_speed
            screen.blit(jump_l[player_anim_count_jump], (player_x, player_y))
        else:
            screen.blit(jump_r[player_anim_count_jump], (player_x, player_y))
        player_anim_count_jump_2 += 0.15
        jumpcount -= 1

    else:
        isJump = False
        jumpcount = 10
        player_anim_count_jump_2 = 0

    if player_anim_count_jump_2 // 1 == 0:
        player_anim_count_jump = 0
    elif player_anim_count_jump_2 // 1 == 1:
        player_anim_count_jump = 1
    elif player_anim_count_jump_2 // 1 == 2:
        player_anim_count_jump = 2
    elif player_anim_count_jump_2 // 1 == 3:
        player_anim_count_jump = 3
    elif player_anim_count_jump_2 // 1 == 4:
        player_anim_count_jump = 0
        player_anim_count_jump_2 = 0

    # if player_anim_count_stoyka_2  == 2:
    # player_anim_count_stoyka =
    if player_anim_count_stoyka_2 // 1 == 0:
        player_anim_count_stoyka = 0
        player_anim_count_stoyka_2 += 0.2
    elif player_anim_count_stoyka_2 // 1 == 1:
        player_anim_count_stoyka = 1
        player_anim_count_stoyka_2 += 0.2
    elif player_anim_count_stoyka_2 // 1 == 2:
        player_anim_count_stoyka = 0
        player_anim_count_stoyka_2 = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    time.tick(12)
