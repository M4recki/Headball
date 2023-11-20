from image_loader import load_image
from player import Player
from computer_opponent import ComputerOpponent
from ball import Ball
from goal import Goal
from score import Score
import pygame as pg
import sys

pg.init()

# Essential variables

width, height = 800, 600

window = pg.display.set_mode((width, height))

font = "game assets/Font/DaddyinspaceDEMO.otf"

player_1_x, player_1_y = 80, 330
player_2_x, player_2_y = 520, 330
ball_x, ball_y = 374, 450

countdown_event = pg.USEREVENT + 2
countdown_font = pg.font.Font(font, 100)
countdown = 4
countdown_text = None

# Load game assets

whistle_sound = pg.mixer.Sound("game assets/Sound/whistle.wav")
score_sound = pg.mixer.Sound(
    "game assets/Sound/mixkit-winning-a-coin-video-game-2069.wav"
)
countdown_sound = pg.mixer.Sound("game assets/Sound/mixkit-soft-bell-countdown-919.wav")

pg.display.set_caption("Headball by Marek B")

pygame_icon = load_image("game assets/PNG/PSD/Game Icon.png")
pg.display.set_icon(pygame_icon)

# Objects

clock = pg.time.Clock()

moving_player = pg.sprite.Group()
player_1 = Player(player_1_x, player_1_y, height)
moving_player.add(player_1)

player_2 = ComputerOpponent(player_2_x, player_2_y, height)
moving_player.add(player_2)

ball = Ball(ball_x, ball_y, width, ball_y)

kick_cooldown = pg.USEREVENT + 3
kick_disabled = False

stadium = load_image("game assets/PNG/Game Background/Stadium.png")
stadium = pg.transform.scale(stadium, (width, height))

goal_1 = Goal(10, 300, 100, 200, flip=True)
goal_2 = Goal(690, 300, 100, 200)

player_1_score = Score(50, 50, font, 32)
player_2_score = Score(600, 50, font, 32)

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


running = True
game_paused = True
pg.time.set_timer(countdown_event, 1000)

# Main loop

while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()
        elif event.type == kick_cooldown:
            kick_disabled = False
        elif event.type == countdown_event:
            player_1.rect.y = player_1_y
            if countdown > 0:
                countdown_sound.play()
                countdown_text = countdown_font.render(
                    str(countdown - 1), True, (255, 255, 255)
                )
                countdown -= 1
            elif countdown == 0:
                countdown_sound.stop()
                countdown_text = countdown_font.render("GO!", True, (255, 255, 255))
                whistle_sound.play()
                countdown -= 1
            else:
                pg.time.set_timer(countdown_event, 0)
                game_paused = False
                countdown_text = None

    # Adding objects to GUI

    add_object(stadium, 0, 0)
    add_object(player_1, player_1_x, player_1_y)
    add_object(player_2, player_2_x, player_2_y)
    add_object(ball, ball_x, ball_y)
    add_object(goal_1, 10, 300)
    add_object(goal_2, 690, 300)
    player_1_score.draw(window)
    player_2_score.draw(window)

    # Movement for player

    if not game_paused:
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
        if (
            keys[pg.K_SPACE]
            and not kick_disabled
            and player_1.rect.colliderect(ball.rect)
        ):
            player_1.kick = True
            player_1.animate(player_1.kick_sprites)
            ball.move_ball([2.5, -15.5])
            kick_disabled = True
            pg.time.set_timer(kick_cooldown, 1)

        if player_1.rect.colliderect(ball.rect):
            ball.move_ball([1.5, 0])

        if player_1.rect.y > 330:
            player_1.rect.y = 330

    # Movement for opponent player

    if ball.rect.x > player_2.rect.x and not game_paused:
        player_2.rect.x += 3
        player_2.run_right = True
        player_2.animate(player_2.run_left_sprites)
    elif ball.rect.x < player_2.rect.x and not game_paused:
        player_2.rect.x -= 3
        player_2.run_left = True
        player_2.animate(player_2.run_right_sprites)
    if player_2.rect.y < 200 and not game_paused:
        player_2.jump()
        player_2.animate(player_2.jump_sprites)
    if player_2.rect.colliderect(ball.rect) and not game_paused:
        ball.move_ball([-1.5, 0])
    if player_2.rect.colliderect(ball.rect) and not kick_disabled:
        player_2.kick = True
        player_2.animate(player_2.kick_sprites)
        ball.move_ball([2.5, -15.5])
        kick_disabled = True
        pg.time.set_timer(kick_cooldown, 50)

    # Check if the ball hit the top of the goal
    if ball.rect.colliderect(goal_1.rect) and ball.rect.top <= goal_1.rect.top:
        ball.velocity[1] = -ball.velocity[1]
    elif ball.rect.colliderect(goal_2.rect) and ball.rect.top <= goal_2.rect.top:
        ball.velocity[1] = -ball.velocity[1]

    # Check if a goal has been scored

    if goal_1.rect.contains(ball.rect):
        score_sound.play()
        game_paused = True
        player_2_score.update(player_2_score.score + 1)

        ball.rect.x = 374
        ball.rect.y = 450
        ball.velocity = [0, 0]

        player_1.rect.x = player_1_x
        player_1.rect.y = player_1_y

        player_2.rect.x = player_2_x
        player_2.rect.y = player_2_y
        player_2.kick = False

        countdown = 4
        pg.time.set_timer(countdown_event, 1000)
    elif goal_2.rect.contains(ball.rect):
        score_sound.play()
        game_paused = True
        player_1_score.update(player_1_score.score + 1)

        ball.rect.x = 374
        ball.rect.y = 450
        ball.velocity = [0, 0]

        player_1.rect.x = player_1_x
        player_1.rect.y = player_1_y

        player_2.rect.x = player_2_x
        player_2.rect.y = player_2_y
        player_2.kick = False

        countdown = 4
        pg.time.set_timer(countdown_event, 1000)

    # Countdown timer after goal has been scored

    if countdown_text:
        window.blit(countdown_text, (ball_x, height // 2))

    # Updating objects

    player_1.update()
    player_2.update()
    ball.update()

    # Display update

    pg.display.flip()
    pg.display.update()
