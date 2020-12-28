"""
File: draw_line.py
Name: Angel Chen
-------------------------
This program creates oval and lines on an instance of GWindow class.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants
SIZE = 20                 # This constant controls the size of the GOval

# Global variable
window = GWindow()
oval = GOval(SIZE, SIZE)  # This creates an oval.
times = 1                 # This calculates the mouse clicked times.


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_oval)


def create_oval(mouse):
    global times

    if times % 2 == 1:        # when mouse clicked times is odd
        window.add(oval, mouse.x - oval.width/2, mouse.y - oval.height/2)
        times += 1
    else:                     # when mouse clicked times is even
        window.remove(oval)   # remove the oval

        # line starts with oval position and ends with mouse clicked position
        line = GLine(oval.x + oval.width/2, oval.y + oval.height/2, mouse.x, mouse.y)
        window.add(line)      # add the line
        times += 1


if __name__ == "__main__":
    main()
