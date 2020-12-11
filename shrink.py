"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage, image that is half size of original image
    """
    img = SimpleImage("images/poppy.png")

    # Make an empty half size canvas
    blank_img = SimpleImage.blank(img.width // 2, img.height // 2)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            blank_pixel = blank_img.get_pixel(x//2, y//2)  # pick only one pixel from every two pixels
            # coloring
            blank_pixel.red = img_pixel.red
            blank_pixel.green = img_pixel.green
            blank_pixel.blue = img_pixel.blue

    return blank_img


def main():
    """
    TODO: resize the image.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
