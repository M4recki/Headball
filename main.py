from image_loader import load_image
from player import Player
import pygame as pg
import sys
from time import sleep


pg.init()

# Essential variables

width, height = 800, 600

player_1_x = 80
player_1_y = 330
player_2_x = 520
player_2_y = 330

clock = pg.time.Clock()

window = pg.display.set_mode((width, height))

pg.display.set_caption("Headball by Marek B")

pygame_icon = load_image("game assets/PSD/Game Icon.png")
pg.display.set_icon(pygame_icon)

# Objects

moving_player = pg.sprite.Group()

player_1 = Player(player_1_x, player_1_y, height)
moving_player.add(player_1)


player_2 = load_image(
    "game assets/Characters/Character 05 - Netherlands/PNG Sequences/Kick/Kick_000.png"
)
player_2 = pg.transform.scale(player_2, (200, 200))

ball = load_image("game assets/pngs/football.png")
ball = pg.transform.scale(ball, (50, 50))

stadium = pg.image.load("game assets/JPG/Game Background/tinywow_Stadium_38893734.png")
stadium = pg.transform.scale(stadium, (width, height))

goal_1 = pg.image.load("game assets/PNG/Elements/goal 1.png")
goal_1 = pg.transform.scale(goal_1, (100, 200))

goal_2 = pg.image.load("game assets/PNG/Elements/goal 2.png")
goal_2 = pg.transform.scale(goal_2, (100, 200))

# Set positions


def add_object(object, x, y):
    if isinstance(object, Player):
        window.blit(object.image, (x, y))
    else:
        window.blit(object, (x, y))


# Main loop

running = True

while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()

    # Adding objects to GUI

    add_object(stadium, 0, 0)
    add_object(player_1, player_1_x, player_1_y)
    add_object(player_2, player_2_x, player_2_y)
    add_object(ball, 374, 450)
    add_object(goal_1, 10, 300)
    add_object(goal_2, 690, 300)

    # Movement

    keys = pg.key.get_pressed()

    if keys[pg.K_w] and player_1.gravity == 0:
        player_1.jump = True
        player_1.gravity = -15
        player_1.animate(player_1.jump_sprites)

    if keys[pg.K_a]:
        player_1_x -= 5
        player_1.run_left = True
        player_1.animate(player_1.run_left_sprites)
    if keys[pg.K_d]:
        player_1_x += 5
        player_1.run_left = True
        player_1.animate(player_1.run_right_sprites)
    if keys[pg.K_SPACE]:
        player_1.kick = True
        player_1.animate(player_1.kick_sprites)

    # Update player_1_x and player_1_y
    player_1_x = player_1.rect.x
    player_1_y = player_1.rect.y

    # Display update

    moving_player.update()
    pg.display.flip()
    pg.display.update()
