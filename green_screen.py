"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            figure_pixel = figure_img.get_pixel(x, y)   # figure
            bigger = max(figure_pixel.red, figure_pixel.blue)
            if figure_pixel.green > bigger*2:  # if the pixel is green,
                pixel_bg = background_img.get_pixel(x, y)
                figure_pixel.red = pixel_bg.red   # then assign the pixel of background to the figure pixel
                figure_pixel.blue = pixel_bg.blue
                figure_pixel.green = pixel_bg.green
    return figure_img


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
