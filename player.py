from pygame import sprite, transform
from image_loader import load_images_for_animation
from random import choice


class Player(sprite.Sprite):
    def __init__(self, x, y, height):
        super().__init__()
        self.is_animating = False
        self.opponents = ("Character 02 - England", "Character 03 - Spain", "Character 04 - Japan", "Character 05 - Netherlands", "Character 06 - Portugal", "Character 07 - Germany", "Character 08 - Italy")
        self.opponent = choice(self.opponents)
        self.run_left_sprites = load_images_for_animation(
            f"game assets/Characters/{self.opponent}/PNG Sequences/Move Backward"
        )
        self.run_right_sprites = load_images_for_animation(
            f"game assets/Characters/{self.opponent}/PNG Sequences/Move Forward"
        )
        self.jump_sprites = load_images_for_animation(
            f"game assets/Characters/{self.opponent}/PNG Sequences/Jump"
        )
        self.kick_sprites = load_images_for_animation(
            f"game assets/Characters/{self.opponent}/PNG Sequences/Kick"
        )
        self.current_sprite = 0
        self.jump = False
        self.run_left = False
        self.run_right = False
        self.kick = False
        self.height = height
        self.animated_sprites = self.run_left_sprites
        self.image = self.run_left_sprites[self.current_sprite]
        self.image = transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(width=150, height=150)
        self.rect.x = x
        self.rect.y = y
        self.y_gravity = 1
        self.jump_height = 15
        self.y_velocity = self.jump_height

    def animate(self, sprites):
        self.is_animating = True
        self.animated_sprites = sprites
        if self.current_sprite < len(sprites) - 1:
            self.current_sprite += 1
        else:
            self.current_sprite = 0
        self.image = sprites[self.current_sprite]
        self.image = transform.scale(self.image, (200, 200))

    def update(self):
        if self.is_animating:
            self.image = self.animated_sprites[self.current_sprite]
            self.is_animating = False
            self.image = transform.scale(self.image, (200, 200))
        if self.jump:
            self.rect.y -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_velocity < -self.jump_height:
                self.jump = False
                self.y_velocity = self.jump_height
                self.animate(self.run_right_sprites)
