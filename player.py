from pygame import sprite, transform
from image_loader import load_images_for_animation


class Player(sprite.Sprite):
    def __init__(self, x, y, height):
        super().__init__()
        self.is_animating = False
        self.run_left_sprites = load_images_for_animation(
            "game assets/Characters/Character 01 - Brazil/PNG Sequences/Move Backward"
        )
        self.run_right_sprites = load_images_for_animation(
            "game assets/Characters/Character 01 - Brazil/PNG Sequences/Move Forward"
        )
        self.jump_sprites = load_images_for_animation(
            "game assets/Characters/Character 01 - Brazil/PNG Sequences/Jump"
        )
        self.kick_sprites = load_images_for_animation(
            "game assets/Characters/Character 01 - Brazil/PNG Sequences/Kick"
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
        self.rect = self.image.get_rect()
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
