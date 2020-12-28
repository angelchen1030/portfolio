"""
File: draw_line_extension.py
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
oval = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_oval)


def create_oval(mouse):
    global oval
    if not oval:              # if not None, meaning True
        oval = GOval(SIZE, SIZE)
        window.add(oval, mouse.x - oval.width/2, mouse.y - oval.height/2)

    else:                     # Oval becomes GOval so it's not None anymore.
        window.remove(oval)   # remove the oval
        # line starts with oval position and ends with mouse clicked position
        line = GLine(oval.x + oval.width/2, oval.y + oval.height/2, mouse.x, mouse.y)
        window.add(line)      # add the line
        oval = None           # reassign oval with None so that it can jump into 'if' zone


if __name__ == "__main__":
    main()
