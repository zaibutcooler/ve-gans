from PIL import Image
import os


def display_image():
    pass


def save_image(tensor, location="./"):

    image = Image.fromarray(tensor)

    if not os.path.exists(location):
        os.makedirs(location)

    image.save(os.path.join(location, "image.jpg"))


def log(text):
    print("")
    print("#############################################\n")
    print(f"{text}\n")
    print("#############################################\n")


import torch


def generate_noise(batch_size, z_dim):

    return torch.randn(batch_size, z_dim)
