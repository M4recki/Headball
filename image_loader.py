from os import path
from pygame import image

# Load images

def load_image(name):
    source_file_dir = path.dirname(path.abspath(__file__))
    img_file_path = path.join(source_file_dir, name)
    return image.load(img_file_path)