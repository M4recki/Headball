from os import path, listdir
from pygame import image

# Load images

def load_image(name):
    source_file_dir = path.dirname(path.abspath(__file__))
    img_file_path = path.join(source_file_dir, name)
    return image.load(img_file_path)

def load_images_for_animation(folder_path):
    images = []
    for im_path in listdir(folder_path):
        images.append(load_image(f'{folder_path}/{im_path}'))
    return images