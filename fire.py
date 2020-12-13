"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original colored image
    :return: SimpleImage, image with fire highlights
    """
    img = SimpleImage('images/greenland-fire.png')
    for pixel in img:
        avg = (pixel.red + pixel.blue + pixel.green) // 3  # grey scale
        if pixel.red > avg * HURDLE_FACTOR:  # detect the pixel with fire and highlight the pixel
            pixel.red = 225
            pixel.blue = 0
            pixel.green = 0
        else:   # turn the rest of pixels into gray scale
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return img


def main():
    """
    TODO: highlight the fire in the image with red.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
