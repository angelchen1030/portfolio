"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:  SimpleImage, image that we want to blur.
    :return: img, blurred image
    """
    # Make an empty canvas
    new_img = SimpleImage.blank(img.height, img.width)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            new_img_pixel = new_img.get_pixel(x, y)

            if x == 0 and y == 0:   # upper left hand corner
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x+1, y)
                a3 = img.get_pixel(x+1, y+1)
                a4 = img.get_pixel(x, y+1)
                red_avg = (a1.red + a2.red + a3.red + a4.red)//4
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue)//4
                green_avg = (a1.green + a2.green + a3.green + a4.green)//4
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            elif x == 0 and y == new_img.height-1:  # bottom left hand corner
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x, y-1)
                a3 = img.get_pixel(x+1, y)
                a4 = img.get_pixel(x+1, y-1)
                red_avg = (a1.red + a2.red + a3.red + a4.red) // 4
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue) // 4
                green_avg = (a1.green + a2.green + a3.green + a4.green) // 4
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            elif x == new_img.width-1 and y == 0:  # upper right hand corner
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x-1, y)
                a3 = img.get_pixel(x, y+1)
                a4 = img.get_pixel(x-1, y+1)
                red_avg = (a1.red + a2.red + a3.red + a4.red) // 4
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue) // 4
                green_avg = (a1.green + a2.green + a3.green + a4.green) // 4
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            elif x == new_img.width-1 and y == new_img.height-1:  # bottom right hand corner
                a1 = img.get_pixel(x, y)   # self
                a2 = img.get_pixel(x, y-1)
                a3 = img.get_pixel(x-1, y)
                a4 = img.get_pixel(x-1, y-1)
                red_avg = (a1.red + a2.red + a3.red + a4.red) // 4
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue) // 4
                green_avg = (a1.green + a2.green + a3.green + a4.green) // 4
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            elif (new_img.width-1) > x > 0 and y == 0:  # top middle
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x, y+1)
                a3 = img.get_pixel(x-1, y)
                a4 = img.get_pixel(x-1, y+1)
                a5 = img.get_pixel(x+1, y)
                a6 = img.get_pixel(x+1, y+1)
                red_avg = (a1.red + a2.red + a3.red + a4.red + a5.red + a6.red) // 6
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue + a5.blue + a6.blue) // 6
                green_avg = (a1.green + a2.green + a3.green + a4.green + a5.green + a6.green) // 6
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            elif (new_img.width-1) > x > 0 and y == new_img.height-1:  # bottom middle
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x, y-1)
                a3 = img.get_pixel(x-1, y)
                a4 = img.get_pixel(x-1, y-1)
                a5 = img.get_pixel(x+1, y)
                a6 = img.get_pixel(x+1, y-1)
                red_avg = (a1.red + a2.red + a3.red + a4.red + a5.red + a6.red) // 6
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue + a5.blue + a6.blue) // 6
                green_avg = (a1.green + a2.green + a3.green + a4.green + a5.green + a6.green) // 6
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            elif x == 0 and (new_img.height-1) > y > 0:  # left middle
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x, y-1)
                a3 = img.get_pixel(x, y+1)
                a4 = img.get_pixel(x+1, y)
                a5 = img.get_pixel(x+1, y-1)
                a6 = img.get_pixel(x+1, y+1)
                red_avg = (a1.red + a2.red + a3.red + a4.red + a5.red + a6.red) // 6
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue + a5.blue + a6.blue) // 6
                green_avg = (a1.green + a2.green + a3.green + a4.green + a5.green + a6.green) // 6
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            elif x == new_img.width-1 and (new_img.height-1) > y > 0:  # right middle
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x, y-1)
                a3 = img.get_pixel(x, y+1)
                a4 = img.get_pixel(x-1, y)
                a5 = img.get_pixel(x-1, y-1)
                a6 = img.get_pixel(x-1, y+1)
                red_avg = (a1.red + a2.red + a3.red + a4.red + a5.red + a6.red) // 6
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue + a5.blue + a6.blue) // 6
                green_avg = (a1.green + a2.green + a3.green + a4.green + a5.green + a6.green) // 6
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

            else:   # middle
                a1 = img.get_pixel(x, y)  # self
                a2 = img.get_pixel(x, y-1)
                a3 = img.get_pixel(x, y+1)
                a4 = img.get_pixel(x-1, y)
                a5 = img.get_pixel(x-1, y-1)
                a6 = img.get_pixel(x-1, y+1)
                a7 = img.get_pixel(x+1, y)
                a8 = img.get_pixel(x+1, y-1)
                a9 = img.get_pixel(x+1, y+1)
                red_avg = (a1.red + a2.red + a3.red + a4.red + a5.red + a6.red + a7.red + a8.red + a9.red) // 9
                blue_avg = (a1.blue + a2.blue + a3.blue + a4.blue + a5.blue + a6.blue + a7.blue + a8.blue + a9.blue) // 9
                green_avg = (a1.green + a2.green + a3.green + a4.green + a5.green + a6.green + a7.green + a8.green + a9.green)//9
                # coloring
                new_img_pixel.red = red_avg
                new_img_pixel.blue = blue_avg
                new_img_pixel.green = green_avg

    return new_img


def main():
    """
    TODO: blur the image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):   # degree of blur
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
