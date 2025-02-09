import pygame
from Hero import MainCharacter
from Villian import MinorVillain
import sys, gif_pygame
from PIL import Image

def resize_gif(input_path, output_path, new_size):
    with Image.open(input_path) as img:
        frames = []
        for frame in range(img.n_frames):
            img.seek(frame)
            resized_frame = img.resize(new_size, Image.LANCZOS)
            frames.append(resized_frame)
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)

class Map(pygame.sprite.Sprite):
    def __init__(self, background, level, *group):
        super().__init__(*group)
        self.gif = gif_pygame.load(background)
        self.level = pygame.transform.scale(pygame.image.load(level), (1200, 800))



screen = pygame.display.set_mode((1200, 800))
all_sprites = pygame.sprite.Group()
map = Map('output.gif', 'sprites/background_1_1.png', all_sprites)
villin = MinorVillain(300, 150, True, all_sprites)
mc = MainCharacter()
while True:
    screen.fill((0, 0, 0))
    villin.update(mc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    map.gif.render(screen, (0, 0))
    screen.blit(map.level, (0, 0))
    screen.blit(villin.current_image, villin.rect)
    pygame.display.update()
    pygame.time.delay(10)