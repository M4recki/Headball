from pygame import sprite, transform
from image_loader import load_image


class Ball(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = load_image("game assets/PNG/Elements/football.png")
        self.image = transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(width=50, height=50)
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.kick = False
        self.gravity = 1
        self.velocity = [0, 0]

    def move_ball(self, force):
        self.velocity[0] += force[0]
        self.velocity[1] += force[1]

    def update(self):
        if self.velocity[0] != 0 or self.velocity[1] != 0:
            self.velocity[1] += self.gravity
            self.velocity[0] *= 0.99

            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

            if self.rect.left < 0:
                self.rect.left = 0
                self.velocity[0] = abs(self.velocity[0])
            if self.rect.right > self.width:
                self.rect.right = self.width
                self.velocity[0] = -abs(self.velocity[0])
            if self.rect.top < 0:
                self.rect.top = 0
                self.velocity[1] = abs(self.velocity[1])
            if self.rect.bottom > 500:
                self.rect.bottom = 500
                self.velocity[1] = -abs(self.velocity[1])

            if self.rect.left < 50 or self.rect.right > self.width - 50:
                self.velocity[0] = -self.velocity[0]
            if self.rect.top < 0 or self.rect.bottom > self.height:
                self.velocity[1] = -self.velocity[1]
