from image_loader import load_image
from player import Player
from computer_opponent import ComputerOpponent
from ball import Ball
from goal import Goal
from score import Score
import pygame as pg
import sys
from time import sleep


pg.init()

# Essential variables

width, height = 800, 600

player_1_x, player_1_y = 80, 330
player_2_x, player_2_y = 520, 330
ball_x, ball_y = 374, 450

clock = pg.time.Clock()

window = pg.display.set_mode((width, height))

pg.display.set_caption("Headball by Marek B")

pygame_icon = load_image("game assets/PNG/PSD/Game Icon.png")
pg.display.set_icon(pygame_icon)

# Objects

moving_player = pg.sprite.Group()
player_1 = Player(player_1_x, player_1_y, height)
moving_player.add(player_1)

player_2 = ComputerOpponent(player_2_x, player_2_y, height)
moving_player.add(player_2)

ball = Ball(ball_x, ball_y, width, ball_y)

kick_cooldown = pg.USEREVENT + 1
kick_disabled = False

stadium = pg.image.load("game assets/PNG/Game Background/Stadium.png")
stadium = pg.transform.scale(stadium, (width, height))

goal_1 = Goal(10, 300, 100, 200, flip=True)
goal_2 = Goal(690, 300, 100, 200)

player_1_score = Score(50, 50, "game assets/Font/DaddyinspaceDEMO.otf", 32)
player_2_score = Score(600, 50, "game assets/Font/DaddyinspaceDEMO.otf", 32)

# Set positions


def add_object(object, x, y):
    if (
        isinstance(object, Player)
        or isinstance(object, Ball)
        or isinstance(object, ComputerOpponent)
        or isinstance(object, Goal)
    ):
        window.blit(object.image, (object.rect.x, object.rect.y))
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
    add_object(ball, ball_x, ball_y)
    add_object(goal_1, 10, 300)
    add_object(goal_2, 690, 300)
    player_1_score.draw(window)
    player_2_score.draw(window)

    # Check for collisions with the top part of the goals

    if ball.rect.colliderect(goal_1.rect) and ball.velocity[1] > 0:
        ball.velocity[1] = -abs(ball.velocity[1])
    elif ball.rect.colliderect(goal_2.rect) and ball.velocity[1] > 0:
        ball.velocity[1] = -abs(ball.velocity[1])

    # Movement for player

    keys = pg.key.get_pressed()

    if keys[pg.K_w] and player_1.rect.y == 330:
        player_1.jump = True
        player_1.animate(player_1.jump_sprites)
    if keys[pg.K_a] and player_1.rect.x > 50:
        player_1.rect.x -= 5
        player_1.run_left = True
        player_1.animate(player_1.run_left_sprites)
    if keys[pg.K_d] and player_1.rect.x < 550:
        player_1.rect.x += 5
        player_1.run_right = True
        player_1.animate(player_1.run_right_sprites)
    if keys[pg.K_SPACE]:
        player_1.kick = True
        player_1.animate(player_1.kick_sprites)
        if player_1.rect.colliderect(ball.rect):
            ball.move_ball([2.5, -7])

    if player_1.rect.colliderect(ball.rect):
        ball.move_ball([1.5, 0])

    # Movement for opponent player

    if ball.rect.x > player_2.rect.x:
        player_2.rect.x += 3
        player_2.run_right = True
        player_2.animate(player_2.run_left_sprites)
    elif ball.rect.x < player_2.rect.x:
        player_2.rect.x -= 3
        player_2.run_left = True
        player_2.animate(player_2.run_right_sprites)

    if player_2.rect.colliderect(ball.rect):
        ball.move_ball([-1.5, 0])

    if player_2.rect.colliderect(ball.rect.inflate(-20, -20)) and not kick_disabled:
        player_2.kick = True
        player_2.animate(player_2.kick_sprites)
        ball.move_ball([-2.5, -7])
        kick_disabled = True
        pg.time.set_timer(kick_cooldown, 2000)

    # Updating objects

    player_1.update()
    player_2.update()
    ball.update()

    # Display update

    pg.display.flip()
    pg.display.update()
