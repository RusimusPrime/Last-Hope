import pygame

class run(pygame.sprite.Sprite):
    def __init__(self, screen, left=False, right=False, player_anim_count_beg=0,
                 player_x=100, player_y=450, player_anim_count_stoyka=0,
                 player_anim_count_jump=0, player_anim_count_jump_2=0, jumpcount=10, jump='False'):
        print(0)
        self.keys = pygame.key.get_pressed()
        screen.fill('white')
        self.jumpcount = jumpcount
        self.player_speed = 10
        self.fps = 10
        self.side = 0
        self.jump = jump
        self.player_x = player_x
        self.player_y = player_y
        self.player_anim_count_beg = player_anim_count_beg
        self.player_anim_count_stoyka = player_anim_count_stoyka
        self.player_anim_count_jump = player_anim_count_jump
        self.player_anim_count_jump_2 = player_anim_count_jump_2
        if self.keys[pygame.K_a] and self.player_x > 10 and self.jumpcount == 10:
            screen.blit(beg_l[self.player_anim_count_beg], (self.player_x, self.player_y))
            self.player_x -= self.player_speed
            self.player_anim_count_beg = (self.player_anim_count_beg + 1) % 3
            self.side = 0

        elif self.keys[pygame.K_d] and self.player_x < 870 and self.jumpcount == 10:
            screen.blit(beg_r[self.player_anim_count_beg], (self.player_x, self.player_y))
            self.player_x += self.player_speed
            self.player_anim_count_beg = (self.player_anim_count_beg + 1) % 3
            self.side = 1
        elif self.jumpcount == 10:
            screen.blit(stoyka[self.player_anim_count_stoyka], (self.player_x, self.player_y))
            self.player_anim_count_stoyka = (self.player_anim_count_stoyka + 1) % 2

        if self.jump == False:
            if self.keys[pygame.K_SPACE]:
                self.jump = True

        if self.jumpcount >= -10 and self.jump == True:
            self.fps = 10
            if self.jumpcount < 0:
                self.player_y += (self.jumpcount ** 2) / 6
            else:
                self.player_y -= (self.jumpcount ** 2) / 6
            if self.keys[pygame.K_d]:
                self.player_x += self.player_speed
                screen.blit(jump_r[self.player_anim_count_jump], (self.player_x, self.player_y))


            elif self.keys[pygame.K_a]:
                self.player_x -= self.player_speed
                screen.blit(jump_l[self.player_anim_count_jump], (self.player_x, self.player_y))


            elif self.player_x > 10 and self.keys[pygame.K_SPACE]:
                self.player_x -= self.player_speed
                screen.blit(jump_l[self.player_anim_count_jump], (self.player_x, self.player_y))


            else:
                screen.blit(jump_r[self.player_anim_count_jump], (self.player_x, self.player_y))

            self.player_anim_count_jump_2 += 0.13
            self.jumpcount -= 1

        else:
            self.jump = False
            self.jumpcount = 10
            self.fps = 10
            self.player_anim_count_jump = 0
            self.player_anim_count_jump_2 = 0

        if self.player_anim_count_jump_2 // 1 == 0:
            self.player_anim_count_jump = 0
        elif self.player_anim_count_jump_2 // 1 == 1:
            self.player_anim_count_jump = 1
        elif self.player_anim_count_jump_2 // 1 == 2:
            self.player_anim_count_jump = 2
        elif self.player_anim_count_jump_2 // 1 == 3:
            self.player_anim_count_jump = 3
        elif self.player_anim_count_jump_2 // 1 == 4:
            self.player_anim_count_jump = 0
            self.player_anim_count_jump_2 = 0





if __name__ == '__main__':
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
    pygame.init()
    pygame.display.set_caption('My game')
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 20
    clock = pygame.time.Clock()
    ex = run(screen, False, False)
    fps = ex.fps
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        ex = run(screen, keys[pygame.K_a], keys[pygame.K_d], ex.player_anim_count_beg, ex.player_x, ex.player_y,
                 ex.player_anim_count_stoyka, ex.player_anim_count_jump, ex.player_anim_count_jump_2, ex.jumpcount, ex.jump)
        fps = ex.fps

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()