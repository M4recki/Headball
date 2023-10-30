from image_loader import load_image
import pygame as pg
import sys


pg.init()

# Essential variables

width, height = 800, 600
clock = pg.time.Clock()
window = pg.display.set_mode((width, height))

pg.display.set_caption("Headball by Marek B")

pygame_icon = load_image("game assets/PSD/Game Icon.png")
pg.display.set_icon(pygame_icon)

# Objects

player_1 = load_image(
    "game assets/Characters/Character 01 - Brazil/PNG Sequences/Kick/Kick_000.png"
)
player_1 = pg.transform.scale(player_1, (200, 200))

player_2 = load_image(
    "game assets/Characters/Character 05 - Netherlands/PNG Sequences/Kick/Kick_000.png"
)
player_2 = pg.transform.scale(player_2, (200, 200))

ball = load_image("game assets/pngs/football.png")
ball = pg.transform.scale(ball, (50, 50))

stadium = pg.image.load("game assets/JPG/Game Background/Stadium.jpg")
stadium = pg.transform.scale(stadium, (width, height))

goal_1 = pg.image.load("game assets/PNG/Elements/goal 1.png")
goal_1 = pg.transform.scale(goal_1, (100, 200))

goal_2 = pg.image.load("game assets/PNG/Elements/goal 2.png")
goal_2 = pg.transform.scale(goal_2, (100, 200))

# Set positions


def add_player_1_at_location(x, y):
    window.blit(player_1, (x, y))


def add_player_2_at_location(x, y):
    window.blit(player_2, (x, y))


def add_ball_at_location(x, y):
    window.blit(ball, (x, y))


def add_goal_1_at_location(x, y):
    window.blit(goal_1, (x, y))


def add_goal_2_at_location(x, y):
    window.blit(goal_2, (x, y))


# Main loop

running = True

while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()

    window.blit(stadium, (0, 0))

    # Adding objects to GUI

    add_player_1_at_location(150, 300)
    add_player_2_at_location(450, 300)

    add_ball_at_location(374, 450)

    add_goal_1_at_location(50, 300)
    add_goal_2_at_location(650, 300)

    # Display update

    pg.display.update()
