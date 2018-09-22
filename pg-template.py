# Pygame template
import pygame as pg


WIDTH = 360
HEIGHT = 480
WINDOW_DIMENSION = (WIDTH, HEIGHT)
FPS = 360
TITLE = "My Awesome PyGame"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialisation pygame et creation de la fenetre
pg.init()
pg.mixer.init()
screen = pg.display.set_mode(WINDOW_DIMENSION)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

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

    # Render
    screen.fill(BLACK)
    pg.display.flip()

pg.quit()
