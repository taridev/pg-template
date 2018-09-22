# Pygame template
import pygame as pg
import os


WIDTH = 800
HEIGHT = 600
WINDOW_DIMENSION = (WIDTH, HEIGHT)
FPS = 360
TITLE = "My Awesome PyGame"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# definition des assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'shuttle2.png')).convert()
        self.image.set_colorkey(BLACK) # Permet de rendre le noir transparent
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 2

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -2
        if self.rect.top < 200:
            self.y_speed = 2
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Initialisation pygame et creation de la fenetre
pg.init()
pg.mixer.init()
screen = pg.display.set_mode(WINDOW_DIMENSION)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    clock.tick(FPS)
    # Events
    for event in pg.event.get():
        # Fermeture de la fenetre
        if event.type == pg.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()
