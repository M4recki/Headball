from pygame import sprite, transform
from image_loader import load_image


class Goal:
    def __init__(self, x, y, width, height, flip=False):
        self.image = load_image("game assets/PNG/Elements/goal.png")
        if flip:
            self.image = transform.flip(self.image, True, False)
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

