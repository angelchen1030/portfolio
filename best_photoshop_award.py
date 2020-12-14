"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.26

# Controls the upper bound for black pixel
BLACK_PIXEL = 100


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            pixel_me = figure_img.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green

            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:  # remove green background
                pixel_bg = background_img.get_pixel(x, y)
                pixel_me.red = pixel_bg.red//1.2
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return figure_img


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background
    """
    space_ship = SimpleImage("image_contest/anya.png")
    figure = SimpleImage("image_contest/angel 2.jpeg")
    space_ship.make_as_big_as(figure)   # adjust two images to same size
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
