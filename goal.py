from pygame import sprite, transform
from image_loader import load_image


class Goal(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = load_image("game assets/PNG/Elements/goal.png")
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
